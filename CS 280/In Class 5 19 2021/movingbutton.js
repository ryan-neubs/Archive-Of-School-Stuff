function moveButton() {
	
	var button = document.getElementById("movingButton");
	
	var offsetX = (Math.random() - 0.5) * 20;
	var offsetY = (Math.random() - 0.5) * 20;
	
	var locTop = button.style.top;
	locTop = parseInt(locTop.match(/\d+/));
	
	var locLeft = button.style.top;
	locLeft = parseInt(locLeft.match(/\d+/));
	
	button.style.top = (locTop + offsetY)+"px";
	button.style.left = (locLeft + offsetX)+"px";
}