var http = require('http');
var https = require('https');

http.createServer(function(req, res) {
  res.writeHead(200, {'Content-Type': 'application/json' });


  var echo = {
    'method': req.method,
    'uri': req.url,
    'headers': req.headers
  };
  res.end(JSON.stringify(echo));
}).listen(3334);

console.log("Started test server on port 3334.");

//TODO generate Self-Signed SSL Cert and spin up HTTPS server to test against.
