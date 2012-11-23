$(document).bind('pageinit', function () {
    $('a#item-submit').bind('tap', function () {
	$('form#new-item-form').submit();
    });
});