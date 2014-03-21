<?php
if(isset($_POST['action']) && !empty($_POST['action'])) {
    $action = htmlspecialchars($_POST['action']);
	switch ($action) {
	    case "left":
	       	exec('PyScriptUmNachLinksZuFahren.py');	    	// HIER EDITIEREN
	        break;
	    case "right":
	        exec('PyScriptUmNachRechtsZuFahren.py');  		// HIER EDITIEREN
	        break;
	    case "usw":
	        exec('usw.py');									// HIER EDITIEREN
	        break;
	}    
}
?>