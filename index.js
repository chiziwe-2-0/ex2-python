var http = require("http");
http.Server((req, res) => res.write('a'.repeat(10)) && res.write('b'.repeat(11)) && res.end('c'.repeat(12))).listen(8888);
