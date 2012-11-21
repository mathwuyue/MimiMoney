$(document).bind('pageinit', function () {
    var startPos = {};

    function calTrackLength(starts, ends) {
	var length = 0;
	for(var i in starts) {
	    var sX = starts[i][0];
	    var sY = starts[i][1];
	    var eX = ends[i][0];
	    var eY = ends[i][1];

	    length = length + Math.sqrt(Math.pow(sX-eX,2)+Math.pow(sY-eY,2));
	}
	return length;
    }
    
    document.addEventListener('touchstart', function (event) {
	if (event.touches.length == 3) 
	    for (var i = 0; i<3; i++) {
		var touch = event.touches[i];
		startPos[touch.identifier] = [touch[i].pageX, touch.pageY];
	    }
    });
	    
    document.addEventListener('touchend', function (event) {
	if (event.touches.length == 3) {
	    var endPos = {};
	    for (var i = 0; i< 3; i++) {
		var touch = event.touches[i];
		endPos[touch.identifier] = [touch.pageX, touch.pageY];
	    }

	    var length = calTrackLength(startPos, endPos);
	    if(length > 300) {
		$.get('logout/', function(data) {
		    window.location.href = 'index.html';
		});
	    }
	}
    });
});