
    


function checkInputs() {
  var isValid = true;
  var numberRegex = /^[+-]?\d+(\.\d+)?([eE][+-]?\d+)?$/;
  $('input[name="steam_pressure"], input[name="steam_temp"],input[name="pipe_length"], input[name="amb_temp"],input[name="maintain_temp"]').each(function(){
  //$('input').filter('[required]').each(function() {


var str = $(this).val();
if(!numberRegex.test(str)) {
    
      $('#calculate').prop('disabled', true);
      $('#calculate').css('background-color', 'grey');

      isValid = false;
      return false;
    }
  });
  if(isValid) {$('#calculate').prop('disabled', false);
     $('#calculate').css('background-color', '#c7ebe8');
             
                }
    
  return isValid;
}
  $(document).on('keyup', 'input[name="steam_pressure"], input[name="steam_temp"],input[name="pipe_length"], input[name="amb_temp"],input[name="maintain_temp"]', function (event) {
//console.log('ok');
//$('input').filter('[required]').on('keyup',function() {
checkInputs();
})

checkInputs();
