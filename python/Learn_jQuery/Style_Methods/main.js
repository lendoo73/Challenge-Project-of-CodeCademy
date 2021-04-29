$(document).ready(() => {
 
  $('.login-button').on('click', () => {
    $('.login-form').toggle();
  });
  
  $('.menu-button').on('mouseenter', () => {
    $('.nav-menu').show().removeClass("hide");
    $('.menu-button').addClass("button-active");
  })
  
  $('.nav-menu').on('mouseleave', () => {
    $('.nav-menu').hide();
    $('.menu-button').css({
      color: "#EFEFEF",
      backgroundColor: "#303030"
    }).animate({
      fontSize: "18px"
    }, 200);
  })
  
}); 
