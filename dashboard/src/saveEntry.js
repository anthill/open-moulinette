"use strict";

module.exports = function(client, data){
    return new Promise(function(resolve, reject){

        client.index(
            {
                index: 'iris',
                type: 'iris',
                body: data.body
            }
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
                



