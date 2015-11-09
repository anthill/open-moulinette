"use strict";

module.exports = function(client, data){
    return new Promise(function(resolve, reject){

        client.bulk({body: data}
            , function (error) {
                if (error) {
                    reject(error);
                }
                else {
                    resolve();
                }
            }
        );

    })
}
                



