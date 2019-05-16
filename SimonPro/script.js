$( document ).ready(function(){
	var i = 0;
	var user = ["Simon", "Jason"];
	$('form').submit(function(){
		if(i){
			i = 0;
		}
		else{
			i = 1;
		}
		var message = $("#chatMessage").val();
		$("#chatMessage").val("");
		$("#listChatRoom").append($("<li>").text(user[i] + ": "+ message));
		return false;
	});
}); 