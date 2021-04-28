$(document).ready(() => {
  // 1
  $(".menu").on("mouseenter", () => {
    $(".nav-menu").show();
  // 2.
  }).on("mouseleave", () => {
    $(".nav-menu").hide();
  });

  // 3 - 4 - 5.
  $(".btn").on("mouseenter", function() {
    $(this).addClass("btn-hover");
  }).on("mouseleave", function() {
    $(this).removeClass("btn-hover");
  });

  // 6, 8.
  $(".postText").on("keyup", event => {
    const post = $(event.currentTarget).val();
    // 9.
    const remaining = 140 - post.length;
    // 11.
    if (remaining <=0) {
      $(".wordcount").addClass("red");
    } else {
      // 12
      $(".wordcount").removeClass("red");
    }
    // 10.
    $('.characters').html(remaining);
  // 7. add focus to the textarea field:  
  }).focus();
}); 
