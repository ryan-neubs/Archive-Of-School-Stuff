//animate.js
//By Ryan Neubauer


 var dom, x, y, firstx = 100, firsty = 900;
 var secondx = 1500, secondy = 900;
 var thirdx = 1500, thirdy = 300;
 var fourthx = 100, fourthy = 300;

 function initText() {
	dom = document.getElementById('W').style;

	var x = dom.left;
	var y = dom.top;

	x = x.match(/\d+/);
	y = y.match(/\d+/);

	pointOne(x, y);
 } 

 function pointOne(x, y) {

	if (x != firstx) 
		if (x > firstx) x--;
		else if (x < firstx) x++;

	if (y != firsty) 
		if (y > firsty) y--;
		else if (y < firsty) y++;

		if ((x != firstx) || (y != firsty)) { 

			dom.left = x + "px";
			dom.top = y + "px";

			setTimeout("pointOne(" + x + "," + y + ")", 1); 
	}
	if (x == firstx && y == firsty){
		pointTwo(x, y);
	}
 }
 function pointTwo(x, y) {

	if (x != secondx) 
		if (x > secondx) x--;
		else if (x < secondx) x++;

	if (y != secondy) 
		if (y > secondy) y--;
		else if (y < secondy) y++;

		if ((x != secondx) || (y != secondy)) { 

			dom.left = x + "px";
			dom.top = y + "px";

			setTimeout("pointTwo(" + x + "," + y + ")", 1); 
	}
	if (x == secondx && y == secondy){
		pointThree(x, y);
	}
 } 
 function pointThree(x, y) {

	if (x != thirdx) 
		if (x > thirdx) x--;
		else if (x < thirdx) x++;

	if (y != thirdy) 
		if (y > thirdy) y--;
		else if (y < thirdy) y++;

		if ((x != thirdx) || (y != thirdy)) { 

			dom.left = x + "px";
			dom.top = y + "px";

			setTimeout("pointThree(" + x + "," + y + ")", 1); 
	}
	if (x == thirdx && y == thirdy){
		pointFour(x, y);
	}
 } 
  function pointFour(x, y) {

	if (x != fourthx) 
		if (x > fourthx) x--;
		else if (x < fourthx) x++;

	if (y != fourthy) 
		if (y > fourthy) y--;
		else if (y < fourthy) y++;

		if ((x != fourthx) || (y != fourthy)) { 

			dom.left = x + "px";
			dom.top = y + "px";

			setTimeout("pointFour(" + x + "," + y + ")", 1); 
	} 
	if (x == fourthx && y == fourthy){
		pointOne(x, y);
	}
 } 
 