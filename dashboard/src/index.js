"use strict";

var fs = require('fs');
var csv = require('csv-parser');
var through = require('through');
var turf = require('turf');

var connectEs = require('./connectEs.js');
var saveEntry = require('./saveEntry.js');
var deleteIndex = require('./deleteIndex.js');
var createindexmapping = require('./createindexmapping.js');


var toKeep = {
    "NB_F102_NB_AIREJEU": "boulodromes",
    "NB_G103": "campings",
    "NB_D306": "alcoolisme",
    "NB_B101": "hypermarches"
}

// load all iris geometry and create a map
var iris = require("../../insee-iris/data/iris.json");
var irisMap = new Map();
iris.features.forEach(feature => {
    irisMap.set(feature.properties.DEPCOM, feature);
})

var batch = [];

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
            .pipe(through(function toEs(row) {

                var stream = this;

                if(irisMap.get(row.COM)) {

                    var center = turf.centroid(irisMap.get(row.COM));

                    var data = {
                        geometry: irisMap.get(row.COM).geometry,
                        center: center.geometry.coordinates
                    }

                    Object.keys(toKeep).map(label => {
                        data[toKeep[label]] = row[label];
                    })                    
                    
                    batch.push({index: {_index: 'iris', _type: 'iris'}});
                    batch.push(data)

                } 

                if (batch.length === 1000) {
                    stream.pause();
                    saveEntry(client, batch)
                    .then(() => {
                        console.log("batch saved");
                        batch = [];
                        stream.resume();
                    })
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
