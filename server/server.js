var express= require('express');
var http = require('http');
var path = require('path');

var app = express();
app.set('port', process.env.PORT || 3000);

app.use('/script',express.static(path.join(__dirname + '/../script')));
app.get('/',function(req, res) {
	res.send('이 서버는 나의 자산 어플의 정보 제공 목적으로 테스트 중입니다.');
});

http.createServer(app).listen(app.get('port'), function() {
	console.log('Start Express server : ' + app.get('port'));
});