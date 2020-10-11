$(document).on('keyup', 'input[name="steam_pressure"]', function (event) {		
		event.preventDefault();
		var input_data = {};
		input_data['steam_pressure'] = this.value;
	    $.ajax({
	        type: 'POST',
	        url: '/sat_temp',
	        dataType: 'json',
	        contentType: 'application/json; charset=utf-8',
	        data: JSON.stringify(input_data),
	        success: function(callback) {	        
				$('input[name="steam_temp"]').val(callback.result);
	        }
	    });
	});
  