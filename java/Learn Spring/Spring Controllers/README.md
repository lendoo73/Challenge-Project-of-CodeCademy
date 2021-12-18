# [Spring controllers](https://www.codecademy.com/courses/learn-spring/lessons/responding-to-requests-with-spring/exercises/introduction)

## [Introduction](https://www.codecademy.com/courses/learn-spring/lessons/responding-to-requests-with-spring/exercises/introduction)

The Spring framework is an incredible resource to help us quickly build RESTful applications. 
The core functionality of these applications lies in their ability to receive requests, route them accordingly, and provide a proper response. 
For a small application, this may not seem like such a tremendous task. 
However, for large enterprise applications receiving thousands of requests per second, how can we be sure each request is routed to the correct destination? 
Moreover, how can we be sure each request receives the proper response?

In this lesson, we will take a look at some of the functionality behind a Spring application 
and we’ll learn how these applications facilitate interaction between clients and servers. 
One of the great features of Spring is being able to encompass all of these key operations with simple, built-in annotations. 
Let’s get started!

## [Mapping Requests in Spring](https://www.codecademy.com/courses/learn-spring/lessons/responding-to-requests-with-spring/exercises/mapping-requests-in-spring)

The term REST stands for REpresentational State Transfer, 
and it describes the architectural technique used to facilitate communication between different systems via the web. 
Stateless requests are sent from a client to either retrieve or make changes to a resource stored on a server. 
The server provides a response based on the information received in the request. 
[Check out this article to learn more about REST architecture.](https://www.codecademy.com/article/what-is-rest)

In order to provide a response to a request, the server maps the request to an endpoint. 
In Spring, a class is marked as a controller and each of its methods is associated with an endpoint. 
The method is called to formulate a response to each request. 
This is facilitated by two important annotations:

* The **`@RestController`** annotation is used to declare a class as a controller that can provide application-specific types of data as part of an HTTP response
* The **`@RequestMapping`** annotation is used to wire request types and endpoints to specific class methods.

The `@RestController` annotation should be added to each class that will handle responses to HTTP requests. 
The `@RestController` combines the functionality of two separate annotations, `@Controller` and `@ResponseBody`.

* **`@Controller`** is used to make a class identifiable to Spring as a component of the web application.
* **`@ResponseBody`** tells Spring to convert the return values of a controller’s methods to JSON and bind that JSON to the HTTP response body. 
Since almost every major programming language offers some type of JSON (JavaScript Object Notation) support, 
we can easily take an object created in Spring and translate it to JSON which can be easily parsed in the HTML and displayed on the page.

`@RequestMapping` accepts several arguments. 
The first, and perhaps most important, is the path. 
The path argument is used to determine where requests are mapped. 
For example, if a user makes a request to get a “book” resource, the server will send the request to a method with the annotation 
`@RequestMapping(path = "/book")` and that method would provide the response.

The `@RequestMapping` annotation also accepts several other arguments including method, params, and consumes. 
Let’s take a look at them.

* **`method`**: allows the developer to specify which HTTP method should be used when accessing the controller method. 
The most common are `RequestMethod.GET`, `...POST`, `...PUT`, and `...DELETE`. 
Since this is an optional argument, if we do not specify an HTTP method it will be defaulted to GET.

* **`params`**: filters requests based on given parameters.

* **`consumes`**: used to specify which media type can be consumed; some common media types are `"text/plain"`, `"application/JSON"`, etc.

```java
@Controller
public class VirtualLibrary{
 
  @RequestMapping("/books/all", RequestMethod.GET)
  public Book getAllBooks() {
    return getBook();
  }
}
```
