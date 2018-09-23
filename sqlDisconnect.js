var mysql = require('mysql');

function sqlDisconnect(con) {
    con.end(function(err) {
	if (err) throw err;
	console.log("Disconnected from database");
    });
}

module.exports = sqlDisconnect;
