"use strict";


var glob = require("glob");
var shapefile = require("shapefile");
var fs =  require("fs");
var csv = require('csv-parser');
var toJSON = require('shp2json')


var departement = 'departement_CC_lambert.csv';

var dep = fs.createReadStream(departement).pipe(csv({separator: ','}));

var CC = 45; // CC is the number of the lamber projection 
var deltaX = 4177302.562212417;
var deltaY = 1297500.1046884255; 
var lw = require("lambert-wilson")(CC, deltaX, deltaY);



var output = fs.createWriteStream("output.geojson");
output.write("[");


glob('CONTOURS-IRIS_1-0__SHP_LAMB93_FXX_2013-01-01/CONTOURS-IRIS/1_DONNEES_LIVRAISON_2014-06-00379/*/*/*.shp', function(err, shapefiles) {
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
			    	console.log("end of file :", file);
			    	return reader.close();
			    } else {
			    	var coord = record.geometry.coordinates[0];
			    	var newCoord = coord.map(function(c) {
			    		var lonlat = lw.toLonLat(c[0], c[1]);
			    		return [lonlat.lon, lonlat.lat];
			    	});
			    	record.geometry.coordinates = [newCoord];
			    	output.write(JSON.stringify(record));
			    	output.write(",");
			    };
			    setImmediate(readNextRecord);
	  		});
		}
		console.log(shapefiles)
	})

});




// testing

// dep.forEach(function(value, key){
// 	o[key] = value;
// });

// for(key in dep) {
//     if(data.hasOwnProperty(key)) {
//         var CC = data[key];
        
//     }
// }


// Object.keys(dep).map(function(key){
// 	return dep[keyIris]
// });


