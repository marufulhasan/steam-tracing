

		var num_pipe = 1;
		var i=1;
    
	$('#add').click(function(){
		num_pipe++;
		i++;
		
		$('#num_segment').html(num_pipe);		
		
		

	    $('#trace_form').append("<input class= 'pipe_"+i+"' id='line_id' name='line_id' type='text' value=''>");	
		$('#trace_form').append('<input class= "pipe_'+i+'"id="pipe_length" name="pipe_length" type="text" value="1000">');


		$('#trace_form').append('<select class= "pipe_'+i+'"  id="pipe_dia" name="pipe_dia"><option value="0.5">1/2</option><option value="0.75">3/4</option><option value="1">1</option><option value="2">2 </option><option value="3">3</option><option value="4">4</option><option value="6">6</option><option value="8" selected="selected">8</option><option value="10">10</option><option value="12">12</option><option value="14">14</option><option value="16">16</option><option value="18">18</option><option value="20">20</option><option value="24">24</option><option value="30">30</option></select>');
		$('#trace_form').append('<select class= "pipe_'+i+'"  id="insulation_type" name="insulation_type"><option value="cal_si">Calcium Silicate</option><option value="fiber_glass">Fiberglass</option></select>');

		$('#trace_form').append('<select class= "pipe_'+i+'"  id="insulation_thickness" name="insulation_thickness"><option value="1">1</option><option value="1.5">1 1/2</option><option value="2" selected="selected">2</option><option value="2.5">2 1/2</option><option value="3">3</option><option value="4">4</option><option value="5">5</option><option value="6">6</option></select>');

		$('#trace_form').append('<input class= "pipe_'+i+'"id="maintain_temp" name="maintain_temp" required type="text" value="150">');
		$('#trace_form').append('<span class= "pipe_'+i+'" name="trace"></span>');
		$('#trace_form').append('<span class= "pipe_'+i+'" name = "tracer_length"></span>');
		$('#trace_form').append('<span class= "pipe_'+i+'" name= "heat_loss"></span>');
		$('#trace_form').append('<span class= "pipe_'+i+'" name= "steam_require"></span>');
		$('#trace_form').append('<input class= "pipe_'+i+'" type="button" value="Remove">');

	$("#pipe_length").attr("required", true);
	
})	

$('#trace_form').on('click', ' [type="button"]', function () {
   
       var class_name = $(this).attr("class");

	   	$('.'+class_name).remove();
	    num_pipe--;
	    $('#num_segment').html(num_pipe);
    
	
    
 	})


