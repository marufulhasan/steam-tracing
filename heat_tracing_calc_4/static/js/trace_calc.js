
$( "#trace_form" ).on( "submit", function( event ) {
	event.preventDefault();
	var input_data = [] ;
	var pipe_data = [], obj;
	$('#trace_form input, #trace_form select').each(function(){
	    obj = {};
	    obj[this.name] = this.value;
	    obj["class"] = this.className
	    pipe_data.push(obj);
	  });

	input_data.push($('#form1').serializeArray());
	input_data.push(pipe_data);	

	//console.log(JSON.stringify(input_data));
	    $.ajax({
	        type: 'POST',
	        url: '/calc_trace',
	        dataType: 'json',
	        contentType: 'application/json; charset=utf-8',
	        data: JSON.stringify(input_data),
	        success: function(callback) {

	        	var total_steam = 0;
	        	console.log(callback.result);
				$.each(callback.result, function(key, value) {
					
					 class_name = '.' +key;					
				     $("[name='trace']" + class_name).text(value.trace);
				     $("[name='heat_loss']" + class_name).text(value.heat_loss);
				     $("[name='steam_require']" + class_name).text(value.steam_require);
				     $("[name='tracer_length']" + class_name).text(value.tracer_length);

				     total_steam += parseFloat(value.steam_require);

			  });	          
				$('#output').html('<strong> Result/ Assumptions</strong> <br> 1. Total required steam is  <strong>' + total_steam.toFixed(3)+ ' lb/hr </strong>' + ' based on wind velocity of '+
					$('#wind_velocity').val() +' mph and ambient temperature of ' + $('#amb_temp').val() +' °F.'+
					'<br> 2. For steam calculation, assumed no steam pressure drop accross tracer, saturated vapor at the tracer inlet and saturated liquid at the tracer outlet.' +
					'<br> 3. Contact manufacturer for detail about selected steam tracer and maximum tracer length.' +
					'<br><strong> Reference</strong> <br>Bondy, Mesagno, J. and Schwartz, M., An Easy Way to Design Steam Tracing for Pipes, Chemical Engineering, August 4, 1986.') ;
	        }
	    });
});