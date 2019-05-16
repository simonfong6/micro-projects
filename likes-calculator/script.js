$( document ).ready(function() {
	
$('#calculate').click(function() {
	
	var numLikes;
	var numMins;
	
	numLikes = Number($("#numLikes").val());
	numMins = Number($("#numMins").val());
	
	console.log(numLikes / numMins);
	
	var quotient = numLikes / numMins;
	
	quotient = parseFloat(Math.round(quotient * 100) / 100).toFixed(2);
	
	if(isNaN(quotient)){
		quotient = "Invalid input! Please use only numbers.";
	}
	
	$( "p" ).text(quotient);
});


});