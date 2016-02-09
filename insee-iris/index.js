"use strict";

require("es6-shim");

var fs =  require("fs");
var glob = require("glob");
var shapefile = require('shapefile');
var Map = require('es6-map');
var proj4 = require('proj4');


// Metropolitan France
proj4.defs["EPSG:2154"] = "+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs";
var epsg2154 = proj4.defs['EPSG:2154'];
var projector = proj4(epsg2154, proj4.WGS84);


// for Guadeloupe, Saint-Barthélemy, Saint-Martin, Martinique 
proj4.defs["EPSG:32620"] = "+proj=utm +zone=20 +ellps=WGS84 +datum=WGS84 +units=m +no_defs ";
var UTM20 = proj4.defs["EPSG:32620"];
var projectorUTM20 = proj4(UTM20, proj4.WGS84);

// for Guyane
proj4.defs["EPSG:2972"] = "+proj=utm +zone=22 +ellps=GRS80 +towgs84=2,2,-2,0,0,0,0 +units=m +no_defs ";
var UTM22 = proj4.defs["EPSG:2972"];
var projectorUTM22 = proj4(UTM22, proj4.WGS84);

// for Réunion
proj4.defs["EPSG:2975"] = "+proj=utm +zone=40 +south +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs ";
var UTM40 = proj4.defs["EPSG:2975"];
var projectorUTM40 = proj4(UTM40, proj4.WGS84);


var output = fs.createWriteStream("data/iris.json");
output.write('{"type": "FeatureCollection", "features": [\n');
 

var shapefiles = [];

(new Promise(function (resolve, reject) {
   glob("data/**/*.shp", {}, function (err, files) {
      if (err) {
         reject(err);
      } else {
         resolve(files);
      }
   });
})).then(function (file) {
      file.forEach(function(fileName) {
         shapefiles.push(fileName);
      })
   })
   .then(function () {
      console.log('Done extracting shapefiles: ', shapefiles.length);

      var nbShapeFileProcessed = shapefiles.length;

      // convert shapefiles to geojson
      var promises = shapefiles.map(function(file){

         return new Promise(function(resolve, reject){

            parseShapeFile(file)
               .then(function(iris){
                  console.log("Nb iris parsed: ", iris.length);

                  // write to file
                  output.write(iris.join(",\n"));
                  if (nbShapeFileProcessed !== 1)
                     output.write(",\n");
                  nbShapeFileProcessed--;
                  resolve();
               })
               .catch(function(error){
                  console.log("Error in parseShapeFile. : ", error);
                  reject();
               })
         });  
      });

      var allFilesProcessed = Promise.all(promises);

      // close the file
      allFilesProcessed
         .then(function(){
            console.log("Finishing")
            output.write("]}");
         })
         .catch(function(error){
            console.log("Could not finish correctly.", error)
         })

   })
  .catch(function (err) {
      console.error(err);
   })


var parseShapeFile = function(file){

   return new Promise(function(resolve, reject){

      var output = [];

      var reader = shapefile.reader(file)
      reader.readHeader(function(error, header) {
         if (error) reject(error);
         readNextRecord();
      }); 

      function readNextRecord() {
         reader.readRecord(function(error, record) {
            if (error)  reject(error);
            if (record === shapefile.end) {
               console.log("end of file : ", file);
               resolve(output);
               return reader.close();
            } else {
               // coordinates to convert
               if(record){
                 
                  var adaptedProjection;
                  switch(record.properties.DEPCOM.substring(0, 3)) {
                     // for Guadeloupe, Saint-Barthélemy, Saint-Martin, Martinique 
                     case '971': // Guadeloupe
                     case '977': // Saint-Barthélemy
                     case '978': // Saint-Martin
                     case '972': // Martinique
                           adaptedProjection = projectorUTM20;
                     break;

                     // for Guyane
                     case '973':
                           adaptedProjection = projectorUTM22;
                     break;

                     // for Réunion
                     case '974':
                           adaptedProjection = projectorUTM40;
                        break;

                     default:
                           adaptedProjection = projector;
                  }

                  var coord = record.geometry.coordinates[0];
         
                  if(record.geometry.type === 'Polygon') {
                     var newCoord = coord.map(function(c){return adaptedProjection.forward(c)});
                  } else { // for MultiPolygon
                     var newCoord = coord.map(function(p){return p.map(function(c){return adaptedProjection.forward(c)})});
                  }

                  var reducedCoords = newCoord.map(function(coords){
                     return reduceLonLat(coords);
                  });

                  record.geometry.coordinates = [reducedCoords];
                  output.push(JSON.stringify(record));
               }
            };
            setImmediate(readNextRecord);
         });
      }
  });
};

function reduceLonLat(list){
   var accuracy = Math.pow(10, 8); // for millimeter precision
   return list.map(function(item){
      return Math.round(item * accuracy) / accuracy; 
   });
}

