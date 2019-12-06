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
      while(i <= events.length/2){


            //normal procedure
            if((i != (events.length-1)) && (odd != true)){
                  var event = '<div class="row">\
                  <div class="col-md-5 event"><div class="row"><div class="col-md-10"><a href="view/' + events[i].id + '">' + events[i].name + '\
                  </a></div></div><div class="row"><div class="col-md-8"><img src="'+ events[i].img + '" class="img-fluid" height="100px" width="200px"></div></div>'
                  + '<div class="row"><div class="col-md-10">' + events[i].when + '</div></div>' + '\
                  </div><div class="col-md-5 event"><div class="row"><div class="col-md-10"><a href="view/' + events[i+1].id + '">' + events[i+1].name + '\
                  </a></div></div><div class="row"><div class="col-md-8"><img src="'+ events[i+1].img + '" class="img-fluid" height="100px" width="200px"></div><div>'
                  + '<div class="row"><div class="col-md-10">' + events[i+1].when + '</div></div></div></div>';
            }
            //last element and odd is true
            else{
                  var event = '<div class="row">\
                  <div class="col-md-5 event" href="view/">' + events[i].id + '<div class="row"><div class="col-md-10"><a href="view/' + events[i].id + '">' + events[i].name + '\
                  </a></div></div><div class="row"><div class="col-md-8"><img src="'+ events[i].img + '" class="img-fluid" height="100px" width="200px"></div></div>'
                  + '<div class="row"><div class="col-md-10">' + events[i].when + '</div></div></div>' + '\
                  <div class="col-md-5"></div></div>';
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