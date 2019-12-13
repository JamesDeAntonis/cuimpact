var display_events = function(events){

      //clear entries to allow for potential update
      $("#allEvents").html("");
     
      if(events.length % 2 == 1){
            var odd = true
      }
      else{
            var odd = false
      }

      var i = 0
      while(i <= events.length){

            //if even 
            if(odd == false){
                  var event = '<div class="row">\
                  <div class="col-md-6"><a href="view/' + events[i].id + '" class="custom-card"><div class="card border border-dark"><img src="'+ events[i].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                  <h5 class="card-title">' + events[i].name + '</h5>' + '\
                  <p class="card-text date">' + events[i].when + '</p>\
                  <p class="card-text group">' + events[i].group + '</p>\
                  <p class="card-text desc">' + events[i].description.substring(0,175) + '...</p></div>' + '\
                  </div></a></div>' + '\
                  <div class="col-md-6"><a href="view/' + events[i+1].id + '" class="custom-card"><div class="card border border-dark"><img src="'+ events[i+1].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                  <h5 class="card-title">' + events[i+1].name + '</h5>' + '\
                  <p class="card-text date">' + events[i+1].when + '</p>\
                  <p class="card-text group">' + events[i+1].group + '</p>\
                  <p class="card-text desc">' + events[i+1].description.substring(0,175) + '...</p></div>' + '\
                  </div></div></div>'
            }
            //if odd
            else{
                  //if last element, accompanying column must be blank
                  if(i == (events.length-1)){
                        var event = '<div class="row">\
                        <div class="col-md-6"><a href="view/' + events[i].id + '" class="custom-card"><div class="card border border-dark"><img src="'+ events[i].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                        <h5 class="card-title">' + events[i].name + '</h5>' + '\
                        <p class="card-text date">' + events[i].when + '</p>\
                        <p class="card-text group">' + events[i].group + '</p>\
                        <p class="card-text desc">' + events[i].description.substring(0,175) + '...</p></div>' + '\
                        </div></a></div>' + '\
                        <div class="col-md-6"></div></div>'
                  }
                  else{
                        var event = '<div class="row">\
                        <div class="col-md-6"><a href="view/' + events[i].id + '" class="custom-card"><div class="card border border-dark"><img src="'+ events[i].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                        <h5 class="card-title">' + events[i].name + '</h5>' + '\
                        <p class="card-text date">' + events[i].when + '</p>\
                        <p class="card-text group">' + events[i].group + '</p>\
                        <p class="card-text desc">' + events[i].description.substring(0,175) + '...</p></div>' + '\
                        </div></a></div>' + '\
                        <div class="col-md-6"><a href="view/' + events[i+1].id + '" class="custom-card"><div class="card border border-dark"><img src="'+ events[i+1].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                        <h5 class="card-title">' + events[i+1].name + '</h5>' + '\
                        <p class="card-text date">' + events[i+1].when + '</p>\
                        <p class="card-text group">' + events[i+1].group + '</p>\
                        <p class="card-text desc">' + events[i+1].description.substring(0,175) + '...</p></div>' + '\
                        </div></div></div>'
                }
            }

            i=i+2

            $("#allEvents").append(event);
      }
}


$(document).ready(function(){
      $("#homeTab").removeClass("active");
      $("#viewAllTab").addClass("active");
      $("#uploadTab").removeClass("active");

      var checkEnv = document.getElementById("environmental-justice");
      var checktrans = document.getElementById("lgbtq");
      var checkIndg = document.getElementById("indigenous-rights");
      var checkImm = document.getElementById("immigration");

      var indigenous_events=[];
      var lgbtq_events=[];
      var environmental_events=[];
      var imm_events=[];
      for (e = 0; e < events.length; e++) {
            if(events[e].issue_tags == "indigenous-rights"){
                  indigenous_events.push(events[e])
            }
            if(events[e].issue_tags == "environmental-justice"){
                   environmental_events.push(events[e])
            }
            if(events[e].issue_tags == "lgbtq"){
                   lgbtq_events.push(events[e])
            }
            if(events[e].issue_tags == "immigration"){
                   imm_events.push(events[e])
            }
      }

      var checkBoxes = document.querySelectorAll(".checkBoxes input");

      for (var i = 0; i < checkBoxes.length; i++) {
          checkBoxes[i].addEventListener("click", filterItems, false);
      }
        
      // the event handler!
      function filterItems(e) {
          if (checkEnv.checked == true) {
              display_events(environmental_events);
          } 
          else if (checktrans.checked == true) {
              display_events(lgbtq_events);
          } 
          else if (checkIndg.checked == true){
              display_events(indigenous_events);
          }
          else if (checkImm.checked == true){
              display_events(imm_events);
          }
          else{
            display_events(events)
          }
      }

      //initial display 
      display_events(events);

      
});