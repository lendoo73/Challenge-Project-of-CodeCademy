# [Flask Forms](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/introduction)

## [Introduction](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/introduction)

An important role of websites is gathering information from the user. 
Whether a user is signing into their Codecademy account, ordering clothes online or leaving feedback for a company, web forms have provided a simple way to enter and submit data over the internet.

The use of forms in a site can be an involved process. 
The designer must gather the right information, display the fields in a pleasing manner and ensure the data is collected correctly. 
Over the years this has become easier thanks to frameworks like Flask, which help streamline the process of displaying fields and gathering data.

This lesson assumes a foundational knowledge of web forms and the steps involved in sending the data to the web server. 
In the following exercises we are going to look at how Flask can help gather data from regular web forms as well as create forms in an entirely new way.

## [Flask Request Object](https://www.codecademy.com/courses/learn-flask/lessons/flask-forms/exercises/flask-request-object)

Every time a client communicates with a server it does so through a *request*. 
By default our Flask routes only support GET requests. 
These are requests for data such as what to display in a browser window. 
When submitting a form through a website, the form data is sent as a POST request. 
This type of request wants to add data to the app. 
Routes can handle POST requests if it is specified in the `methods` argument of the `route()` decorator:
```
@app.route("/", methods=["GET", "POST"])
```

























































