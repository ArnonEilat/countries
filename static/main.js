jQuery(document).ready(function() {
	jQuery('#vmap').vectorMap({
		map : 'world_en',
		backgroundColor : 'transparent',
		color : '#ffffff',
		hoverOpacity : 0.7,
		selectedColor : '#666666',
		enableZoom : true,
		showTooltip : true,
		values : sample_data,
		scaleColors : [ '#C8EEFF', '#006491' ],
		normalizeFunction : 'polynomial',
		onRegionClick : function(element, code, region) {
			// var message = 'You clicked "' + region
			// + '" which has the code: '
			// + code.toUpperCase();
			location.href = window.location.origin + "/" + code;

			// alert(message);
		}
	});
});

var datalist = document.getElementById("countriesList");
var input = document.getElementById("countriesIpt");

input.addEventListener("keyup", function(event) {
	if (event.which === 13) {

		var name = input.value;
		for ( var i = 0; i < countriesObjArr.length; i++) {
			if (countriesObjArr[i].name === name) {
				location.href = window.location.origin + "/"
						+ countriesObjArr[i].code;
				return;
			}
		}
		alert("There is no country with ths name ("+input.value+")");
	}
}, false);
