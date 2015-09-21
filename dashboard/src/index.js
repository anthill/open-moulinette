"use strict";

var fs = require('fs');
var csv = require('csv-parser');
var through = require('through');
var turf = require('turf');

var connectEs = require('./connectEs.js');
var saveEntry = require('./saveEntry.js');
var deleteIndex = require('./deleteIndex.js');
var createindexmapping = require('./createindexmapping.js');

// load all iris geometry and create a map
var iris = require("../../insee-iris/data/iris.json");
var irisMap = new Map();
iris.features.forEach(feature => {
    irisMap.set(feature.properties.DEPCOM, feature);
})

connectEs()
.then(function(client){
    deleteIndex(client)
    .then(function(){
        createindexmapping(client)
        .then(function(){
            console.log("ES clean and ready.");

            // steam through the csv and load to ES
            fs.createReadStream("../../insee/data/output.csv")
            .pipe(csv({separator: ';'}))
            .pipe(through(row => {

                if(irisMap.get(row.COM)) {
                    
                    row["geometry"] = irisMap.get(row.COM).geometry;
                    var center = turf.centroid(irisMap.get(row.COM));

                    row["center"] = center.geometry.coordinates;

                    saveEntry(client, {body: row})
                    .catch(function(err){
                        console.error('Es store error', err);
                    });
                } 

            }))
            .on('close', function(){
                console.log("Finished loading in ES.")
            })

        })
        .catch(function(err){
            console.error("Couldn't create index", err);
        });
    })
    .catch(function(err){
        console.error("Couldn't delete index", err);
    });

})
.catch(function(err){
    console.error("Couldn't connect to es", err);
});
