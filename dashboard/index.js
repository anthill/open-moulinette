"use strict";

var fs = require('fs');
var csv = require('csv-parser');
var through = require('through');

// load all iris geometry and create a map
var iris = require("../insee-iris/data/iris.json");

// steam through the csv and load to ES
fs.createReadStream("../insee/data/output.csv")
    .pipe(csv({separator: ';'}))
    .pipe(through(function(row){

        console.log(row)

    }))
    .on('close', function(){
        console.log("Finished processing file.")
    })
