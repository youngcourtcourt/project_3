$('#magnitude').slider({
	formatter: function(value) {
		return 'Current value: ' + value;
	}
});

var slider = new Slider('#magnitude', {
	formatter: function(value) {
		return 'Current value: ' + value;
	}
});