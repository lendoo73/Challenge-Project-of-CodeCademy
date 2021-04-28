$(document).ready(() =>{
  // 1. create an event handler
  $(".hint-box").on("click", () => {
    // 2.
    $(".hint").slideToggle(300);
  });

  // 3. wrong answer click event:
  const $wrongAnswers = $(".wrong-answer-one, .wrong-answer-two, .wrong-answer-three")
  $wrongAnswers.on("click", function () {
    // 4. wrong answer to fade out
    $(event.target).fadeOut("slow");
    // 5. a frowny face to appear
    $(".frown").show();
  });

  // 6. correct answer click event:
  $(".correct-answer").on("click", () => {
    // 7. frowny face to disappear
    $(".frown").hide();
    // 8. smiley face appear 
    $(".smiley").show();
    // 9. the wrong answers fade away
    $wrongAnswers.fadeOut("slow");
  });

  // 10. reset the quiz
  $(".reset").click(() => {
    location.reload();
  });
});
