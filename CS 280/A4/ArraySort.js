//Array Sort
//By Ryan Neubauer and Gavin Roy

function checkNum(item) {return typeof item === 'number';}
function checkString(item) {return typeof item === 'string';}
function checkSign(item) {return Math.sign(item) === 1;}

function chunk(array) {
	var nums = array.filter(checkNum);
	strings = array.filter(checkString);
	return [nums, strings];
}
function arraySort(array) {
	chunks = chunk(array);
	var nums = chunks[0];
	strings = chunks[1];
	sortNum = nums.sort(function(a, b){return a - b});
	posNums = array.filter(checkSign);
	total = 0;
	for(var i = 0; i < posNums.length; i++) {
		total += posNums[i];
	}
	var average = total/posNums.length;
	return [sortNum, strings.join('#'), average];
}
