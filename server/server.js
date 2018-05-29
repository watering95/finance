var express= require('express');
var http = require('http');

var app = express();
app.set('port', process.env.PORT || 3000);

app.use('/script', express.static(__dirname + "/script"));
app.use(function(req, res, next) {
	res.writeHead('200', {'Content-Type':'text/html;charset=utf-8'});
	res.write('<!DOCTYPE html>');
	res.write('<html>');
	res.write('<head>');
	res.write('<script type="text/javascript" src="/script/test.js"></script>');
	res.write('</head>');
	res.write('<body>');
	res.write('</body>');
	res.end('</html>');
});

http.createServer(app).listen(app.get('port'), function() {
	console.log('Start Express server : ' + app.get('port'));
});