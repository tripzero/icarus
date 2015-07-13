//ws: a node.js websocket implementation
//wscat = command line util. either acts as server (--listen) or client (--connect)
//https://github.com/websockets/ws

//Documentation
//using ws and express is a dependency downloaded via vvv; had to get past intel proxy for express download
//http://expressjs.com/starter/installing.html
//seems like we don't use express in the end; make sure to verify there are no other dependencies. 
//TODO: FIGURE OUT WHICH VERSION OF NODEJS IS BEING UTILIZED.

var sys = require("sys");

/*var httpServ = require('http');
var reactor = null;
reactor = httpServ.createServer(  ).listen( 8080 );
reactor.listen(8080);
*/



//////////////////////

http = require('http');
console.log("Hello World");
app = http.createServer();

//app.use(express.static(__dirname + '/public'));
app.listen(8080);

//example server use
var WebSocketServer = require('ws').Server
wss = new WebSocketServer({server: app});


wss.on('open', function open() {
  console.log('connected');
  //ws.send(Date.now().toString(), {mask: true});
});

wss.on('connection', function connection(client) {
	console.log('nodejs websocket is connected');
    client.on('message', function incoming(message) {
        console.log('received: %s', message); //parse the json we are sending (python code; the tilt percent.)
    }); //console.debug?
});


wss.on('close', function() {
    console.log('stopping client interval');
    clearInterval(id);
});

sys.puts("End World");




//server sending broadcast data 
/*wss.broadcast = function broadcast(data) {
  	wss.clients.forEach(function each(client) {
    client.send(data);
    sys.puts("Hello World");
  	});
    wss.send('something'); //tilt data?
};

var msg = wss.broadcast("test broadcast msg")
console.log(msg)
*/
///////////////////////////////////////////////////////


/*
//Sending and receiving text data
var WebSocket = require('ws');
//how to import my autobahn websocket?
var ws = new WebSocket('127.0.0.1:8080'); //autobahn server for run_actuators: 127.0.0.1/880

ws.on('open', function open() {
  ws.send('Sending a test msg');
});

ws.on('message', function(data, flags) {
  // flags.binary will be set if a binary data is received.
  // flags.masked will be set if the data was masked.
});


//Sending binary data
var WebSocket = require('ws');
var ws = new WebSocket('ws://www.host.com/path');

ws.on('open', function open() {
  var array = new Float32Array(5);

  for (var i = 0; i < array.length; ++i) {
    array[i] = i / 2;
  }

  ws.send(array, { binary: true, mask: true });
});*/