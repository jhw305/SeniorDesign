var sqlQuery = require('./sqlQuery.js');

function sqlGetStores(con, sqlGetStoresCallback) {
    sqlQuery(con, 'SELECT * FROM store', sqlGetStoresCallback);
}

module.exports = sqlGetStores;	
