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

















