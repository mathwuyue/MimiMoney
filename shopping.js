$(document).bind('pageinit', function () {
    $('a#item-submit').bind('tap', function () {
	$('form#new-item-form').submit();
    });

    $('a#item-submit').bind('click', function () {
	$('form#new-item-form').submit();
    });
});