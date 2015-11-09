"use strict";


module.exports = function(client){
    return new Promise(function(resolve, reject){

        client.indices.exists(
            { 
                index: "iris",
                ignoreUnavailable: true
            }
            , function (error, indexExists) {
                if (error) {
                    reject(error);
                }
                else {
                    if (indexExists){
                        client.indices.delete(
                            {
                                index: "iris"
                            }
                            , function (error) {
                                if (error) {
                                    reject(error);
                                }
                                else {
                                    console.log("Droped iris index");
                                    resolve();
                                }
                            }
                        );
                    } else {
                        console.log("Iris doesn't exists.");
                        resolve();
                    }
                }
            }
        );
    })
}
                



