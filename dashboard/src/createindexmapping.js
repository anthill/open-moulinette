"use strict";


module.exports = function(client){
    return new Promise(function(resolve, reject){

        var body = {
            "mappings": {

                "iris": {
                    properties : {
                        "geometry":     {"type" : "geo_point",  "store" : true }
                    }
                }
            }
        };

        client.indices.create(
            {
                index: "iris",
                body: body
            }
            , function (error) {
                if (error) {
                    reject(error);
                }
                else {
                    console.log("Created iris index with mapping.")
                    resolve();
                }
            }
        );

    })
}
                



