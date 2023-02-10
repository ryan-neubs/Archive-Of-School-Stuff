// primes.js
// Generate prime factors, given an input
//		from the user

	upper = prompt("Enter an input value: ", "");
	
	for (var index = 2; index < upper; index++) {
		var factorFound = false;
		for (factor = 2; factor < Math.sqrt(index); factor++) {
			if (index % factor ==0) {
				factorFound = true;
			}
		}
		if (!factorfound) {
			document.write(index, "<br/>");
		}
	}