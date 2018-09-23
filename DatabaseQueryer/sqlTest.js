var sqlConnect = require('./sqlConnect.js');
var sqlQuery = require('./sqlQuery.js');
var sqlDisconnect = require('./sqlDisconnect.js');
var sqlGetStores = require('./sqlGetStores');
var sqlGetItemsFromStore = require('./sqlGetItemsFromStore');

var con = sqlConnect();
sqlGetStores(con, console.error);
sqlGetItemsFromStore(con, 1162, console.error);
sqlDisconnect(con);
