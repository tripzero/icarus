//ws: a node.js websocket implementation
//wscat = command line util. either acts as server (--listen) or client (--connect)
//https://github.com/sitegui/nodejs-websocket

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
    ws.on('message', function(message) {
        console.log('received: %s', message);
    });
    ws.send('something');
});
