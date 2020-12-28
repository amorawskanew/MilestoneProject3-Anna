let clipboard = new Clipboard('.copy-icon');

$(document).ready(function(){
/*
    jQuery for MaterializeCSS initialization for drop down menu
*/
$(document).ready(function () {
    
    $(".sidenav").sidenav({edge: "right"});
});
/*
    MaterializeCSS initialization for home page card deck image gallery
*/
document.addEventListener("DOMContentLoaded",function(){
    const gallery= document.querySelectorAll(".materialboxed");
    M.Materialbox.init(gallery,{});
});



  // Or with jQuery inicialization for add new cocktail folder

  $(document).ready(function(){
    $('select').formSelect();
  });

   // button inicialization 
$(document).ready(function(){
    $('.modal').modal();
  });
 
    // Fades out flash message after it has been read by user
    $("#flash-msg").delay(4500).fadeOut("slow");

});