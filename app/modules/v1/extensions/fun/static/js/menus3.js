$(document).ready(function(){
	$(".panel a").click(function(e){
		e.preventDefault();
		var style = $(this).attr("class");
		$("#modafesto").removeAttr("class").addClass("navigation").addClass(style);
	});
});
