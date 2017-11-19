
$(document).ready(function(){
 $(".test").on("click", function() {
  $(".me").hide();
 $(".otch").hide();
  $(".dannie_body").toggle();

});
 $(".test1").on("click", function() {
 $(".dannie_body").hide();
 $(".otch").hide();
 $(".me").toggle();
});
  $(".test2").on("click", function() {
   $(".dannie_body").hide();
   $(".me").hide();
   $(".otch").toggle();
});
        });

