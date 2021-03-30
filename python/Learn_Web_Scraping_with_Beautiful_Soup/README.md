#### WEB SCRAPING WITH BEAUTIFUL SOUP
# [Introduction](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/introduction)

Often times you’ll find the perfect website that has all the data you need, but there’s no way to download it. 
This is where BeautifulSoup comes in handy to scrape the HTML. 
If we find the data we want to analyze online, we can use BeautifulSoup to grab it and turn it into a structure we can understand. 
This Python library, which takes its name from a song in Alice in Wonderland, allows us to easily and quickly take information from a website and put it into a DataFrame.

# [Rules of Scraping](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/rules-of-scraping)
When we scrape websites, we have to make sure we are following some guidelines so that we are treating the websites and their owners with respect.

Always check a website’s Terms and Conditions before scraping. 
Read the statement on the legal use of data. 
Usually, the data you scrape should not be used for commercial purposes.

Do not spam the website with a ton of requests. 
A large number of requests can break a website that is unprepared for that level of traffic. 
As a general rule of good practice, make one request to one webpage per second.

If the layout of the website changes, you will have to change your scraping code to follow the new structure of the site.

# [Requests](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/requests)
In order to get the HTML of the website, we need to make a request to get the content of the webpage. 
To learn more about requests in a general sense, you can check out [this article](https://www.codecademy.com/articles/http-requests).

Python has a `requests` library that makes getting content really easy. 
All we have to do is import the library, and then feed in the URL we want to `GET`:
```
import requests
 
webpage = requests.get('https://www.codecademy.com/articles/http-requests')
print(webpage.text)
```
This code will print out the HTML of the page.

# [The BeautifulSoup Object](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/the-beautifulsoup-object)
When we printed out all of that HTML from our request, it seemed pretty long and messy. 
How could we pull out the relevant information from that long string?

BeautifulSoup is a Python library that makes it easy for us to traverse an HTML page and pull out the parts we’re interested in. 
We can import it by using the line:
```
from bs4 import BeautifulSoup
```
Then, all we have to do is convert the HTML document to a BeautifulSoup object!

If this is our HTML file, rainbow.html:
```
<body>
  <div>red</div>
  <div>orange</div>
  <div>yellow</div>
  <div>green</div>
  <div>blue</div>
  <div>indigo</div>
  <div>violet</div>
</body>
```
```
soup = BeautifulSoup("rainbow.html", "html.parser")
```
`"html.parser"` is one option for parsers we could use. 
There are other options, like `"lxml"` and `"html5lib"` that have different advantages and disadvantages, but for our purposes we will be using "html.parser" throughout.

With the requests skills we just learned, we can use a website hosted online as that HTML:
```
webpage = requests.get("http://rainbow.com/rainbow.html", "html.parser")
soup = BeautifulSoup(webpage.content)
```
When we use BeautifulSoup in combination with pandas, we can turn websites into DataFrames that are easy to manipulate and gain insights from.

# [Object Types](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/object-types)
BeautifulSoup breaks the HTML page into several types of objects.

## Tags
A Tag corresponds to an HTML Tag in the original document. 
These lines of code:
```
soup = BeautifulSoup('<div id="example">An example div</div><p>An example p tag</p>')
print(soup.div)
```
Would produce output that looks like:
```
<div id="example">An example div</div>
```
Accessing a tag from the BeautifulSoup object in this way will get the first tag of that type on the page.

You can get the name of the tag using `.name` and a dictionary representing the attributes of the tag using `.attrs`:
```
print(soup.div.name)
print(soup.div.attrs)
```
```
div
{'id': 'example'}
```

## NavigableStrings
NavigableStrings are the pieces of text that are in the HTML tags on the page. 
You can get the string inside of the tag by calling .string:
```
print(soup.div.string)
```
```
An example div
```

# [Navigating by Tags](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/navigating-by-tags)
To navigate through a tree, we can call the tag names themselves. 
Imagine we have an HTML page that looks like this:
```
<h1>World's Best Chocolate Chip Cookies</h1>
<div class="banner">
  <h1>Ingredients</h1>
</div>
<ul>
  <li> 1 cup flour </li>
  <li> 1/2 cup sugar </li>
  <li> 2 tbsp oil </li>
  <li> 1/2 tsp baking soda </li>
  <li> ½ cup chocolate chips </li> 
  <li> 1/2 tsp vanilla <li>
  <li> 2 tbsp milk </li>
</ul>
```
If we made a soup object out of this HTML page, we have seen that we can get the first `h1` element by calling:
```
print(soup.h1)
```
```
<h1>World's Best Chocolate Chip Cookies</h1>
```
We can get the children of a tag by accessing the `.children` attribute:
```
for child in soup.ul.children:
    print(child)
<li> 1 cup flour </li>
<li> 1/2 cup sugar </li>
<li> 2 tbsp oil </li>
<li> 1/2 tsp baking soda </li>
<li> ½ cup chocolate chips </li> 
<li> 1/2 tsp vanilla <li>
<li> 2 tbsp milk </li>
```
We can also navigate up the tree of a tag by accessing the `.parents` attribute:
```
for parent in soup.li.parents:
    print(parent)
```
This loop will first print:
```
<ul>
<li> 1 cup flour </li>
<li> 1/2 cup sugar </li>
<li> 2 tbsp oil </li>
<li> 1/2 tsp baking soda </li>
<li> ½ cup chocolate chips </li>
<li> 1/2 tsp vanilla </li>
<li> 2 tbsp milk </li>
</ul>
```
Then, it will print the tag that contains the `ul` (so, the `body` tag of the document). 
Then, it will print the tag that contains the `body` tag (so, the `html` tag of the document).

# [Website Structure](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/website-structure)
When we’re telling our Python script what HTML tags to grab, we need to know the structure of the website and what we’re looking for.

Many browsers, including Chrome, Firefox, and Safari, have Dev Tools that help you inspect a webpage and see what HTML elements it is composed of.

First, learn [how to use DevTools](https://www.codecademy.com/articles/use-devtools).

Then, when you’re preparing to scrape a website, first inspect the HTML to see where the info you are looking for is located on the page.

# [Find All](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/find-all)
If we want to find all of the occurrences of a tag, instead of just the first one, we can use `.find_all()`.

This function can take in just the name of a tag and returns a list of all occurrences of that tag.
```
print(soup.find_all("h1"))
```
```
['<h1>World's Best Chocolate Chip Cookies</h1>', '<h1>Ingredients</h1>']
```
`.find_all()` is far more flexible than just accessing elements directly through the soup object. 
With `.find_all()`, we can use regexes, attributes, or even functions to select HTML elements more intelligently.

## Using Regex
What if we want every `<ol>` and every `<ul>` that the page contains? 
We can select both of these types of elements with a regex in our `.find_all()`:
```
import re
soup.find_all(re.compile("[ou]l"))
```
What if we want all of the `h1` - `h9` tags that the page contains? 
Regex to the rescue again!
```
import re
soup.find_all(re.compile("h[1-9]"))
```

## Using Lists
We can also just specify all of the elements we want to find by supplying the function with a list of the tag names we are looking for:
```
soup.find_all(['h1', 'a', 'p'])
```

## Using Attributes
We can also try to match the elements with relevant attributes. 
We can pass a dictionary to the `attrs` parameter of `find_all` with the desired attributes of the elements we’re looking for. 
If we want to find all of the elements with the "banner" class, for example, we could use the command:
```
soup.find_all(attrs={'class':'banner'})
```
Or, we can specify multiple different attributes! What if we wanted a tag with a `"banner"` class and the id `"jumbotron"`?
```
soup.find_all(attrs={'class':'banner', 'id':'jumbotron'})
```

## Using A Function
If our selection starts to get really complicated, we can separate out all of the logic that we’re using to choose a tag into its own function. 
Then, we can pass that function into `.find_all()`!
```
def has_banner_class_and_hello_world(tag):
    return tag.attr('class') == "banner" and tag.string == "Hello world"
 
soup.find_all(has_banner_class_and_hello_world)
```
This command would find an element that looks like this:
```
<div class="banner">Hello world</div>
```
but not an element that looks like this:
```
<div>Hello world</div>
```
Or this:
```
<div class="banner">What's up, world!</div>
```

# [Select for CSS Selectors](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/select-for-css-selectors)
Another way to capture your desired elements with the `soup` object is to use CSS selectors. 
The `.select()` method will take in all of the CSS selectors you normally use in a `.css` file!
```
<h1 class='results'>Search Results for: <span class='searchTerm'>Funfetti</span></h1>
<div class='recipeLink'><a href="spaghetti.html">Funfetti Spaghetti</a></div>
<div class='recipeLink' id="selected"><a href="lasagna.html">Lasagna de Funfetti</a></div>
<div class='recipeLink'><a href="cupcakes.html">Funfetti Cupcakes</a></div>
<div class='recipeLink'><a href="pie.html">Pecan Funfetti Pie</a></div>
```
If we wanted to select all of the elements that have the class `'recipeLink'`, we could use the command:
```
soup.select(".recipeLink")
```
If we wanted to select the element that has the id `'selected'`, we could use the command:
```
soup.select("#selected")
```
Let’s say we wanted to loop through all of the links to these funfetti recipes that we found from our search.
```
for link in soup.select(".recipeLink > a"):
  webpage = requests.get(link)
  new_soup = BeautifulSoup(webpage)
```
This loop will go through each link in each `.recipeLink` div and create a soup object out of the webpage it links to. 
So, it would first make soup out of `<a href="spaghetti.html">Funfetti Spaghetti</a>`, then `<a href="lasagna.html">Lasagna de Funfetti</a>` , and so on.

# [Reading Text](https://www.codecademy.com/courses/learn-web-scraping/lessons/web-scraping-with-beautiful-soup/exercises/reading-text)
When we use BeautifulSoup to select HTML elements, we often want to grab the text inside of the element, so that we can analyze it. 
We can use `.get_text()` to retrieve the text inside of whatever tag we want to call it on.
```
<h1 class="results">Search Results for: <span class='searchTerm'>Funfetti</span></h1>
```
If this is the HTML that has been used to create the `soup` object, we can make the call:
```
soup.get_text()
```
Which will return:
```
'Search Results for: Funfetti'
```
Notice that this combined the text inside of the outer `h1` tag with the text contained in the `span` tag inside of it! 
Using `get_text()`, it looks like both of these strings are part of just one longer string. 
If we wanted to separate out the texts from different tags, we could specify a separator character. 
This command would use a `.` character to separate:
```
soup.get_text('|')
```
Now, the command returns:
```
'Search Results for: |Funfetti'
```
