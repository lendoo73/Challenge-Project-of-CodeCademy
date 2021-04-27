// 1. 
$(document).ready(
  () => {
    // 2. add click event handlers to multiple element: 
    // https://api.jquery.com/multiple-selector/
    $("#cart, #account, #help").on("click", () => {
      // 3. appear drop-down menu 
      $(event.target.nextElementSibling).show();
    });
    // 4. add mouseleave event handler
      const $dropdownMenu = $(".dropdown-menu");
      $dropdownMenu.on("mouseleave", () => {
      // 5. disappear drop-down menu
      $dropdownMenu.hide();
    });
  }
);
