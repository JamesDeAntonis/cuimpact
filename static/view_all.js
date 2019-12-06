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
      $("#searchTab").removeClass("active");
      $("#uploadTab").removeClass("active");

      //initial display 
      display_events(events);


      var checkEnv = document.getElementById("environmental-justice");
      var checktrans = document.getElementById("trans-rights");
      var checkIndg = document.getElementById("indigenous-rights");

      if (checkEnv.checked == true){
            events = events[3]
            display_events(events);
      } 
      if (checktrans.checked == true){
            events = events[2]
            display_events(events);
      } 
      if (checkIndg.checked == true){
            events = [events[0], events[1]]
            display_events(events);
      } 

});