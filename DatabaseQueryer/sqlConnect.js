var mysql = require('mysql');

function sqlConnect() {
    var con = mysql.createConnection({
      server: "72.211.224.233\\sql",
      port: "3306",
      user: "realsenor",
      password: "password",
      database: "realsenordb",
      insecureAuth : true
    });

    con.connect(function(err) {
	if (err) throw err;
	console.log("Connected to database");
    });
    return con;
}

module.exports = sqlConnect;
