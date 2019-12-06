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
            if(odd != true){
                  var event = '<div class="row">\
                  <div class="col-md-6"><div class="card"><img src="'+ events[i].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                  <h5 class="card-title">' + events[i].name + '</h5>' + '\
                  <p class="card-text">' + events[i].description.substring(0,150) + '...</p></div>' + '\
                  <ul class="list-group list-group-flush"><li class="list-group-item"><h5>' + events[i].when + '</h5></li>' + '\
                  <li class="list-group-item">' + events[i].group + '</li></ul>' + '\
                  <a href="view/' + events[i].id + '"><div class="card-body viewEvBut">View Event</div></a></div></div>' + '\
                  <div class="col-md-6"><div class="card"><img src="' + events[i+1].img + '" class="card-img-top"><div class="card-body">' + '\
                  <h5 class="card-title">' + events[i+1].name + '</h5>' + '\
                  <p class="card-text">' + events[i+1].description.substring(0,150) + '...</p> </div>' + '\
                  <ul class="list-group list-group-flush"><li class="list-group-item"><h5>' + events[i+1].when + '</h5></li>' + '\
                  <li class="list-group-item">' + events[i+1].group + '</li></ul>' + '\
                  <a href="view/' + events[i+1].id + '"><div class="card-body viewEvBut">View Event</div></a></div>'
            }
            //if odd
            {
                  //if last element, accompanying column must be blank
                  if(i == (events.length-1)){
                        var event = '<div class="row">\
                        <div class="col-md-6"><div class="card"><img src="'+ events[i].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                        <h5 class="card-title">' + events[i].name + '</h5>' + '\
                        <p class="card-text">' + events[i].description.substring(0,150) + '...</p></div>' + '\
                        <ul class="list-group list-group-flush"><li class="list-group-item"><h5>' + events[i].when + '</h5></li>' + '\
                        <li class="list-group-item">' + events[i].group + '</li></ul>' + '\
                        <a href="view/' + events[i].id + '"><div class="card-body viewEvBut">View Event</div></a></div></div>' + '\
                        <div class="col-md-6"></div></div>'
                  }
                  else{
                        var event = '<div class="row">\
                        <div class="col-md-6"><div class="card"><img src="'+ events[i].img + '" class="card-img-top img-fluid"><div class="card-body">' + '\
                        <h5 class="card-title">' + events[i].name + '</h5>' + '\
                        <p class="card-text">' + events[i].description.substring(0,150) + '...</p></div>' + '\
                        <ul class="list-group list-group-flush"><li class="list-group-item"><h5>' + events[i].when + '</h5></li>' + '\
                        <li class="list-group-item">' + events[i].group + '</li></ul>' + '\
                        <a href="view/' + events[i].id + '"><div class="card-body viewEvBut">View Event</div></a></div></div>' + '\
                        <div class="col-md-6"><div class="card"><img src="' + events[i+1].img + '" class="card-img-top"><div class="card-body">' + '\
                        <h5 class="card-title">' + events[i+1].name + '</h5>' + '\
                        <p class="card-text">' + events[i+1].description.substring(0,150) + '...</p> </div>' + '\
                        <ul class="list-group list-group-flush"><li class="list-group-item"><h5>' + events[i+1].when + '</h5></li>' + '\
                        <li class="list-group-item">' + events[i+1].group + '</li></ul>' + '\
                        <a href="view/' + events[i+1].id + '"><div class="card-body viewEvBut">View Event</div></a></div>'
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

      //initial display 
      display_events(events);


      var checkEnv = document.getElementById("environmental-justice");
      var checktrans = document.getElementById("trans-rights");
      var checkIndg = document.getElementById("indigenous-rights");

      var indigenous_events=[];
      var trans_events=[];
      var environmental_events=[];
      for (e = 0; e < events.length; e++) {
            if(events[e].issue_tags == "indigenous-rights"){
                  indigenous_events.push(events[e])
            }
            if(events[e].issue_tags == "environmental-justice"){
                   environmental_events.push(events[e])
            }
            if(events[e].issue_tags == "trans-rights"){
                   trans_events.push(events[e])
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
              display_events(trans_events);
          } 
          else if (checkIndg.checked == true){
              display_events(indigenous_events);
          }
          else{
            display_events(events)
          }
      }



      
});