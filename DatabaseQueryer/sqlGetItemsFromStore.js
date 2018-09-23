var sqlQuery = require('./sqlQuery.js');

function sqlGetItemsFromStore(con, storeID, sqlGetItemsFromStoreCallback) {
    sqlQuery(con, 'SELECT * FROM items WHERE storeid = ' + storeID, sqlGetItemsFromStoreCallback);
}

module.exports = sqlGetItemsFromStore;	
