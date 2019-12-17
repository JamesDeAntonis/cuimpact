$(document).ready(function(){

  $("#homeTab").removeClass("active");
  $("#viewAllTab").removeClass("active");
  $("#uploadTab").removeClass("active");

  //initial display 
  $("#nameView").html(name);
  var imag = '<img src = "' + img + '" class="img-fluid center-block" height="400px" width="400px">'
  $("#imgView").html(imag);
  $("#descriptionView").html(description);
  $("#whenView").html(when);
  $("#locView").html(loc);
  var buttonLinks = ' <a class="btn btn-primary btnVi" href="' + link + '" target="_blank"> RSVP on Facebook</a><a class="btn btn-warning btnVi" href="mailto:'+ email +'">Email</a>'
  $("#buttons").html(buttonLinks)
});

       
        