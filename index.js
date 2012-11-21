$(function() {
    $('form#login-form').submit(function () {
	$.post('login/', $('form#login-form').serialize(), function(data) {
	    if (data == 'failed') {
		$('#login-error').popup('open');
		return true;
	    }
	    window.location.href = 'main/';
	});
	return false;
    });

    $('form#create-user-form').submit(function () {
	var p1 = $('form#create-user-form input[name="password"]').val();
	var p2 = $('form#create-user-form input[name="password2"]').val();
	if (p1 == p2) {
	    $.post('users/', $('form#create-user-form').serialize(), function (data) {
		if (data == 'failed') {
		    $('#user-exist').popup('open');
		    return true;
		}

		window.location.href = 'main/';
	    });

	    return false;
	}

	$('#wrong-password').popup('open');
	return false;
    });
		    
});
