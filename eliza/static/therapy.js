
function operate(data){
	var resp = JSON.parse(data.responseText)
	$("#conversation").append("Eliza: "+resp.eliza);
	$("#conversation").append("<br>");
	$("#conversation").append("<br>");
	$("#therapy_text").val("");
}


function get_therapy(event,name){
	var key = event.keycode || event.which;
	if(key === 13){
		console.log("ENTER");
		var human_input = $("#therapy_text").val();
		$("#conversation").append(name+ ": " +human_input);
		$("#conversation").append("<br>");

		var human_obj = new Object();
		human_obj.human = human_input;
   		var human_json = JSON.stringify(human_obj);
		jQuery.ajax ({
			url: "/eliza/DOCTOR",
			type: "POST",
			data: human_json,
			dataType: "json",
			contentType: "application/json; charset=utf-8",
			complete: operate
		});
	}
}
