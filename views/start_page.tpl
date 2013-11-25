<!DOCTYPE html>
<html>
<head>
<title>Hackita - Countries Of The World</title>

<link href="static/jqvmap/jqvmap/jqvmap.css" media="screen" rel="stylesheet" type="text/css" />
<link href="static/style.css" media="screen" rel="stylesheet" type="text/css" />

<script	src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min.js" type="text/javascript"></script>
<script src="static/jqvmap/jqvmap/jquery.vmap.js" type="text/javascript"></script>
<script src="static/jqvmap/jqvmap/maps/jquery.vmap.world.js" type="text/javascript"></script>
<script src="static/jqvmap/jqvmap/data/jquery.vmap.sampledata.js" type="text/javascript"></script>



</head>
<body>
	<h1>Countries Of The World</h1>
	<div id="vmap" style="width: 600px; height: 400px;"></div>

<input id="countriesIpt" placeholder="Enter name of Country" name="countriesIpt" list="countriesList" />
<datalist id="countriesList">
% for d in countries:
<option>{{d}}</option>
% end
</datalist>

<script type="text/javascript">
var countriesObjArr=new Array();

% for d in countries:
countriesObjArr.push({"name":"{{d}}", "code": "{{countries[d]}}"});
% end
</script>

<script src="static/main.js" type="text/javascript"></script>

</body>
</html>
