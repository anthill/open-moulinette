"use strict";

var fs =  require("fs");
var csv = require('csv-parser');
var shapefile = require('shapefile');
var through = require("through");
var Map = require('es6-map');
var proj4 = require('proj4');


// define projection
var proj4 = require('proj4');
proj4.defs["EPSG:2154"] = "+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs";
var epsg2154 = proj4.defs['EPSG:2154'];
var projector = proj4(epsg2154, proj4.WGS84);


var output = fs.createWriteStream("data/output.geojson");
output.write("[");
 

// unzip files
var Zip = require('node-7z'); // Name the class as you want!
var unzipTask = new Zip();

var shapefiles = [];

unzipTask.extractFull('data/iris-france.7z', 'data/iris')
  .progress(function (file) {
    file.forEach(function(fileName) {
      if (/\.shp$/.test(fileName)) {
        shapefiles.push("data/iris/" + fileName);
      } 
    })
  })
  .then(function () {
    console.log('Done extracting shapefiles: ', shapefiles.length);

    // convert shapefiles to geojson
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

              // convert coordinates  in WGS
              var coord = record.geometry.coordinates[0];

              var newCoord = coord.map(function(c) {
                return projector.forward(c);
              });
            record.geometry.coordinates = [newCoord];
            output.write(JSON.stringify(record));
            output.write(",");

          };
          setImmediate(readNextRecord);
        });
      }

    });

  })
  .catch(function (err) {
    console.error(err);
  })
