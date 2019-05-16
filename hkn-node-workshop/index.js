// load the express module
var app = require('express')();
// load the http module and create a server
var server = require('http').createServer(app);
// load socket io and listen on server
var io = require('socket.io').listen(server);

// route handler
app.get('/', function(req, res){
  res.sendfile('index.html');
});

// when io.sockets receives connectoin
io.sockets.on('connection', function(socket){
  console.log('a user connected');
  // when socket receives disconnect
  socket.on('disconnect', function(){
      console.log('user disconnected');
  });
  // when socket receives chat message 
  socket.on('chat message', function(msg){
    console.log('message: ' + msg);
    io.emit('chat message', msg); 
  });
});

// tell server to listen for connections
var port = process.env.PORT || 3000; 
server.listen(port, function() {
  var addr = server.address(); 
  console.log('app listening on http://' + addr.address + ':' + addr.port);   
}); 
