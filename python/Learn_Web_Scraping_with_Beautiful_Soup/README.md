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
