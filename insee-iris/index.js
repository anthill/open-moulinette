"use strict";


var fs =  require("fs");
var glob = require("glob");
var csv = require('csv-parser');
var shapefile = require('shapefile');
var through = require("through");


var departement = 'data/departement_CC_lambert.csv';

var depCcList = [];

var dep = fs.createReadStream(departement).pipe(csv({separator: ','})).pipe(through(function(data){ depCcList.push({'departement' : parseInt(data.Departement),'lambertCc' : parseInt(data.lambert_cc)});}));


var deltaX = 0;
var deltaY = 0; 


var output = fs.createWriteStream("output.geojson");
output.write("[");
 
var Zip = require('node-7z'); // Name the class as you want!
var myTask = new Zip();

var compteur = 0;

myTask.extractFull('data/CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01.7z', 'data/CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01')
// Equivalent to `on('data', function (files) { // ... });`
.progress(function (file) {
  file.forEach(function(fileName) {
    if (/\.shp$/.test(fileName)) {
        compteur++;
    } 
  })
})
// When all is done
.then(function () {
  console.log('Extracting done!');
  console.log(compteur);
})
// On error
.catch(function (err) {
  console.error(err);
})

glob('data/CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01/CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01/CONTOURS-IRIS/1_DONNEES_LIVRAISON_2014-06-00379/*/*/*.shp', function(err, shapefiles) {
  shapefiles.forEach(function(file){
    
    var reader = shapefile.reader(file)
    reader.readHeader(function(error, header) {
      if (error) throw error;
      readNextRecord();
    }); 

    function readNextRecord() {
      reader.readRecord(function(error, record) {
        if (error) {
          console.log("error file : ", file)
          throw error;
        }
        if (record === shapefile.end) {
          output.write("]");
          console.log("end of file : ", file);
          return reader.close();
        } else {
          console.log("begin of file : ", file);
          // Departement number (a string with special CORSE number(2A / 2B))
          var depStr = record.properties.DEPCOM.substring(0, 2);

          // find lambertCc for the departement number
          depCcList.forEach(function(data) {
            if(String(data.departement) === depStr) {
              var lambertCc = data.lambertCc;
            
              var lw = require("lambert-wilson")(lambertCc, deltaX, deltaY);

              var coord = record.geometry.coordinates[0];

              var newCoord = coord.map(function(c) {
                var lonlat = lw.toLonLat(c[0], c[1]);
                return [lonlat.lon, lonlat.lat];
              });
            record.geometry.coordinates = [newCoord];
            output.write(JSON.stringify(record));
            output.write(",");
            }
          });
        };
        setImmediate(readNextRecord);
      });
    }

    console.log(shapefiles)
  });

});
