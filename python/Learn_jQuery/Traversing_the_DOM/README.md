#### TRAVERSING THE DOM

# [The DOM Tree](https://www.codecademy.com/courses/learn-jquery/lessons/traversing-the-dom/exercises/the-dom-tree)

jQuery makes it easy to target HTML elements by tag name, class, and id. 
We can also dynamically target a single element in a given class by accessing an event’s `.currentTarget` attribute. 
In this lesson, we’ll go even further. 
You will learn how to target elements based on their position relative to other elements.

Before we begin, let’s review the Document Object Model or DOM. 
The DOM is a tree of objects based on the HTML document that is created by the browser when it loads a page. 
Every element in this page exists on some branch of the tree, with elements above it, and possibly next to or below it.
```html
<div class='parent'>
  <div class='child' id='sibling1'>
    <p class='grandchild'></p>
  </div>
  <div class='child' id='sibling2'></div>
  <div class='child' id='sibling3'></div>
</div>
```
Elements inside other elements are considered descendants. 
We use family words to refer to these relationships. 
For instance, an outer `<div>` would be considered the parent of any `<div>` element inside it (those with class `'child'` above). 
Any other `<div>`s inside of `'parent'` on the same level as `'child'` are considered siblings of each other. 
A `<p>` in any `'child'` would itself be a child of the `'child'` element that contains it and a grandchild of `'parent'`.

# [Children](https://www.codecademy.com/courses/learn-jquery/lessons/traversing-the-dom/exercises/children)

According to the DOM tree, the outermost element is the parent of all elements inside of it. 
Therefore, the HTML elements inside of the outer element are children. 
The jQuery `.children()` method allows us to target these elements.
```html
<div class='parent' id='holder'>
  <div>Child <span>1</span></div>
  <div>Child <span>2</span></div>
  <div>Child <span>3</span></div>
</div>
```
```javascript
const $kids = $('#holder').children();
$kids.on('click', event => {
  $(event.currentTarget).css('border', '1px solid black');
});
```
* In the example above, the `$kids` variable refers to all children of the element with id `'holder'` (the divs inside `'#holder'`). 
* The .`on()` method adds the click event handler to these `$kids`. 
* When one of them is clicked, jQuery will add a border around it that is `1px` wide and `solid black`.

It is important to note that only the direct descendants of `'#holder'` are considered children. 
Any elements inside the child elements of `'#holder'`, such as the `<span>` elements, will not be targeted by the `.children()` method.

# [Parent & Siblings](https://www.codecademy.com/courses/learn-jquery/lessons/traversing-the-dom/exercises/siblings-parent)

In addition to the `.children()` method we covered in the last exercise, there are two methods you can use to select the parent and siblings of an element.
```js
$('.choice').on('click', event => {
  $(event.currentTarget).parent().hide();
});
```
In the example above, the .parent() method targets the parent element of '.choice' elements and removes it from the DOM.

$('.choice').on('click', event => {
  $(this).siblings().removeClass('selected');
  $(event.currentTarget).addClass('selected');
});
In the code above, the .siblings() method targets elements adjacent to the clicked '.choice' and removes the 'selected' class from any previously clicked '.choice's. Then the 'selected' class is added only to the clicked '.choice'.













