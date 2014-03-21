<!DOCTYPE html>
<html>
<head>
	<script type="text/javascript" src="jquery-2.1.0.min.js"></script>
	<script type="text/javascript">
		var button='';
		function scriptAusfuehren(){
			$.ajax({ url: './Script.php',
     	    	data: {action: button},
        		type: 'post'
       		});
		}
	</script>
</head>
<body>
<button onclick="button='left';scriptAusfuehren()">Left</button>
<button onclick="button='right';scriptAusfuehren()">Right</button>
</body>
</html>	
