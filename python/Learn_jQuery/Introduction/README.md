#### JQUERY SETUP

# [Why jQuery?](https://www.codecademy.com/courses/learn-jquery/lessons/jquery-setup/exercises/why-jquery)

JavaScript is the most widely-used language for adding dynamic behavior to web pages. 
The JavaScript community contributes to a collection of libraries that extend and ease its use. 
In this course, you will learn about jQuery, a JavaScript library that makes it easy to add dynamic behavior to HTML elements.

Let’s look at an example of how JavaScript is used to add dynamic behavior to a web page (don’t worry about understanding the code).
```JavaScript
const login = document.getElementById('login');
const loginMenu = document.getElementById('loginMenu');
 
login.addEventListener('click', () => {
  if(loginMenu.style.display === 'none'){
    loginMenu.style.display = 'inline';
  } else {
    loginMenu.style.display = 'none';
  }
});
```
In this example, JavaScript is used to apply behavior to an HTML element with id `login`. 
The behavior allows a user to click a **LOGIN** button that toggles a login form.

The code below accomplishes the same behavior with jQuery.
```JavaScript
$('#login').click(() => {
  $('#loginMenu').toggle()
});
```
In this example, the same toggle functionality is accomplished using just three lines of code.
