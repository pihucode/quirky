$(document).ready(function() {

  // when menu icon is clicked, display a div containing nav links
  navMenu = document.getElementById('menu-icon');
  navMenu.addEventListener("click",function(){
      $("#nav-display").removeClass("hidden");
  });

  // when closeButton is clicked, hide the div containing nav links
  $("#close-button").click(function () {
      $("#nav-display").addClass("hidden");
  });

  // TODO: print contents of div

});