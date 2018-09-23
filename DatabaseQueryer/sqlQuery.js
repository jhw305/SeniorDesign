function sqlQuery(con, query, sqlQueryCallback) {
    con.query(query, function(err, result) {
        if (err) {
          console.log('Error executing query', err);
          sqlQueryCallback(err);
          con.end(function(err) {
            if (err) {
              console.log('Error closing connection', err);
            } else {
              console.log('Connection closed');
            }
	  });
	  return;
        }
        console.log('Query executed: ' + query);
        sqlQueryCallback(null, JSON.stringify(result));
    });
}
module.exports = sqlQuery;

