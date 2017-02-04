function get_therapy(event){
	var key = event.keycode || event.which;
	if(key === 13){
		console.log("ENTER");
		var human_input = $("#therapy_text").val();

		var human_obj = new Object();
		human_obj.human = human_input;
   		var human_json = JSON.stringify(human_obj);
		jQuery.ajax ({
			url: "/eliza/DOCTOR",
			type: "POST",
			data: human_json,
			dataType: "json",
			contentType: "application/json; charset=utf-8",
			complete: function(data){
				console.log("COMPLETE");
				console.log(data.responseText);
				alert("DOCTOR response: \"" + data.responseText+"\"");
			},
		});
	}
}
