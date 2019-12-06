var upload_event = function(new_item){
	var new_event= new_item;

	$.ajax({
		type:"POST",
		url: "/save_event",
		dataType: "json",
		contentType: "application/json; charset=utf-8",
		data: JSON.stringify(new_event),
		success: function(result){
			//add writing to writing variable
			events.unshift(new_event)
			current_id += 1
			location.href = "/view_all"
		},
        error: function(request, status, error){

        	$("#content").append("<div id=\"error\">Error! Event could not be uploaded.</div>")
			console.log("Error")
			console.log(request)
			console.log(status)
			console.log(error)
        }
		})
};


$(document).ready(function(){

  $("#homeTab").removeClass("active");
  $("#viewAllTab").removeClass("active");
  $("#uploadTab").addClass("active");

	$("#addEvent").click(function(){
		var new_event = {
    		"name": $("#eventName").val(),
    		"group": $("#groupName").val(),
    		"group-email": $("#emailName").val(),
            "description": $("#descriptionEvent").val(), 
            "issue-tags": $("#genre").val(),
            "facebook-link": $("#eventLink").val(),
            "img": $("#imageLink").val(),
            "when":$("#whenName").val()
            "location": $("#locationName").val()
        };
		upload_event(new_event);
	});
});