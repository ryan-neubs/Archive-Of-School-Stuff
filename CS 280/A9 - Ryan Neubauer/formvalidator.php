function checkName() {
	$myName = $_POST["fname"];
	if(preg_match(/^[A-Z][a-z]+, ?[A-Z]\.?, ?[A-Z][a-z]+$/) {
		echo The name you entered "$myName" is not in the correct form. <br/>
			 The correct form is: 
			 first-name, middle-initial, first-name
	}
}