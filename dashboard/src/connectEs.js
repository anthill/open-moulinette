var elasticsearch = require('elasticsearch');

var client = new elasticsearch.Client({
    host: process.env.ELASTICSEARCH_HOST + ':9200',
    log: 'error',
    apiVersion: '1.7'
});

module.exports = function(){
    return new Promise(function(resolve){
        
        (function tryConnect(){
            client.ping(
                {
                  requestTimeout: 2000
                }
                , function(err) {
                if(err) {
                    //console.log(err);
                    tryConnect();
                }
                else {
                    console.log("Connected to ES");
                    resolve(client);
                }
            });
        })();
        
    });
};