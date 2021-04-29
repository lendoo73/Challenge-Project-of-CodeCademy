$(document).ready(() => {
  // 1 - 2: add a keyup event
  $("#text").keyup(event => {
    // 3:
    $(".preview").html($(event.currentTarget).val());
  });
   
  // 4: attach a change event to font family
  $("#font").change(event => {
    // 5. add type effect
    $(".preview").css("font-family", $(event.currentTarget).val());
  });

  // 6. add another change event handler to the weight menu:
  $("#weight").change(event => {
    $(".preview").css("font-weight", $(event.currentTarget).val());
  });

  // 7.
  $("#size").keyup(event => {
    // 8.
    const fontSize = $(event.currentTarget).val() + "px";
    // 9. 
    $(".preview").css("font-size", fontSize);
  });

})
