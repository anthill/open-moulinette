"use strict";


module.exports = function(client){
    return new Promise(function(resolve, reject){

        var body = {
            "mappings": {

                "iris": {
                    properties : {
                        "boulodromes": {"type" : "float",     "store" : true },
                        "campings": {"type" : "float",    "store" : true },
                        "alcoolisme": {"type" : "float",    "store" : true },
                        "hypermarches": {"type" : "float",    "store" : true },
                        "geometry": {"type" : "geo_shape", "store" : true },
                        "center": {"type" : "geo_point", "store" : true }
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
                



