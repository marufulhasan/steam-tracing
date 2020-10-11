	$(document).on('keyup', 'input[name="steam_pressure"], input[name="steam_temp"],input[name="pipe_length"], input[name="amb_temp"],input[name="maintain_temp"]', function (event) {
		this.value = this.value.replace(/[^0-9\.]/g,'');
	});