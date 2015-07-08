//ws: a node.js websocket implementation
//wscat = command line util. either acts as server (--listen) or client (--connect)
//https://github.com/sitegui/nodejs-websocket
//https://github.com/websockets/ws

var sys = require("sys");
sys.puts("Hello World");

//example client use	
var WebSocket = require('ws')
  , ws = new WebSocket('ws://www.host.com/path');
ws.on('open', function() {
    ws.send('something');
});
ws.on('message', function(message) {
    console.log('received: %s', message);
});

//example server use
var WebSocketServer = require('ws').Server
  , wss = new WebSocketServer({port: 8080});
wss.on('connection', function(ws) {
	console.log('nodejs websocket is connected')
    ws.on('message', function(message) {
        console.log('received: %s', message); //parse the json we are sending (python code; the tilt percent.)
    });
    ws.send('something');
});

///////////////////////////////////////////////////////



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
});