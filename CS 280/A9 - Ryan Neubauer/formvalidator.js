//formvalidator.js
//by Ryan Neubauer

function checkName() {
	var myName = document.getElementById("fname");
	var pos = myName.value.search(/^[A-Z][a-z]+, ?[A-Z]\.?, ?[A-Z][a-z]+$/);
	if (pos != 0) {
		alert("The name you entered (" + myName.value + 
			") is not in the correct form. \n" +
			"The correct form is: " +
			"first-name, middle-initial, first-name");
	}
}

function checkAddress() {
	var address = document.getElementById("address");
	var pos = address.value.search(/^\d+\s{1}([A-Z][a-z]+\s{0,2}){1,2}$/);
	if (pos != 0) {
		alert("Invalid Address. The address entered: " + address.value +
		" is in incorrect form.\n" +
		"Please make sure your address starts with a number, followed by " +
		"one or two street names starting with a capital letter and separated with 1-2 spaces. " +
		"Only letters can be used in street names.");
	}
}

function checkCardNum() {
	var cnum = document.getElementById("cnum");
	var pos = cnum.value.search(/^(\d{4}-){3}\d{4}$/);
	var pos1 = cnum.value.search(/^\d{16}$/);
	if (pos != 0 && pos1 != 0) {
		alert("Invalid card number. The number entered: " + cnum.value + 
		" is in an invalid form. \n" +
		"Please enter it in the correct form: " +
		"####-####-####-####");
	}
}

function checkPhoneNum(){
	var phoneNum = document.getElementById("phonenum").value;
	pos = phoneNum.search(/^(\d{3}-){2}\d{4}$/);
	pos1 = phoneNum.search(/^\d{10}$/);
	pos2 = phoneNum.search(/^(\d{3}\.){2}\d{4}$/);
	if (pos != 0 && pos1 != 0 && pos2 != 0) {
		alert("Please use one of the correct phone formats: \n###.###.#### \n###-###-#### \n##########");
	}
}

function checkEmail() {
	var emailID = document.getElementById("email").value;
         atpos = emailID.indexOf("@");
         dotpos = emailID.lastIndexOf(".");
         
         if (atpos < 1 || (dotpos - atpos < 2)) {
            alert("Please enter correct email ID");
            document.getElementById("email").value = ""
         }
}

function checkQuantity(value) {
	var value;
	if(isNaN(value)) {
		alert("Order quantities must only include a number 0-110.\n" +
		"Please enter 0 for items you will not purchase.");
	}
	if(value < 0 || value > 110) {
		alert("Order quantities must only include a number 0-110.\n" +
		"Please enter 0 for items you will not purchase.");
	}
}

function checkPurchaseAmt() {
	var item1 = document.getElementById("kcQuantity").value;
	item2 = document.getElementById("pkQuantity").value;
	item3 = document.getElementById("svQuantity").value;
	item4 = document.getElementById("flagQuantity").value;
	total = item1 + item2 + item3 + item4;
	if(total == 0){
		alert("You must order at least one item");
	}
}

