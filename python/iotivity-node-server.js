//template
// Server that illustrates the action of the entity handler. client.observable.js contains a client
// that issues a request that causes the entity handler to fire.

var intervalId,
	iotivity = require( "iotivity" ),
	handle = {};

iotivity.OCInit( 134.134.139.74, 8080, iotivity.OCMode.OC_SERVER ); 
//name of nodejs server?

//<ipaddress> , <portnumber> , OC_CLIENT_SERV

intervalId = setInterval( function() {
	iotivity.OCProcess();
}, 100 ); //why is this 100?

iotivity.OCCreateResource(
	handle,
	"tiltPercentage",
	//"oc.mi.def",
	//"/light/1",
	function( flag, request ) {
		console.log( "OCCreateResource() handler: Entering" );
		return iotivity.OCEntityHandlerResult.OC_EH_OK;
	},
	iotivity.OCResourceProperty.OC_DISCOVERABLE
);

process.on( "SIGINT", function() {
	console.log( "SIGINT: Quitting..." );
	clearInterval( intervalId );
	iotivity.OCStop();
	process.exit( 0 );
} );