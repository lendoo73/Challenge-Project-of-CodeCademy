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

## [Defining Base Paths]()
We’ve discussed how to use `@RequestMapping` at the method level, now let’s discover how it can be used at the class level.

When the `@RequestMapping` data annotation is used at the class level, the specified path argument will become the base path. 
For example, a class with the data annotation `@RequestMapping("/books")` will map all appropriate requests to this class, 
and in this case, “/books” becomes the base path. 
Methods in this class can be further mapped, as shown in the previous exercise. 
In the example shown below, “/books” is now the base path and the `getBookThumbnails` method is associated with the endpoint “/books/thumbnails”:

```java
@RestController
@RequestMapping("/books")
public class VirtualLibrary
{
  @RequestMapping(value = "/thumbnails", method = RequestMethod.GET)
  public String[] getBookThumbnails() {
    //returns thumbnails for all available titles
  }
}
```

Note: When specifying a selection from the `RequestMethod` enum, be sure to import the annotation using:

```
org.springframework.web.bind.annotation.RequestMethod
```

## [Using HTTP Method Annotations](https://www.codecademy.com/courses/learn-spring/lessons/responding-to-requests-with-spring/exercises/using-http-method-annotations )

In the Mapping Requests exercise, we discussed several parameters for the `@RequestMapping` data annotation. 
One of the arguments mentioned was the method argument. 
As a reminder, the method argument is used to specify which HTTP method the given method should use. 
However, the method argument is optional. 
If we forget to specify it, our method defaults to responding to GET requests. 
For this reason, we should always specify the HTTP method type.

In addition to using the method argument of the `@RequestMapping` annotation, 
Spring also offers several annotations which can be used to map to common request types. 
These annotations perform the same function as `@RequestMapping`. 
As shown in the example below, using the path and method argument of the `@RequestMapping` annotation 
is equivalent to just passing in a path to one of the HTTP method annotations. 
The four common HTTP methods we use to interact with resources are GET, POST, PUT, and DELETE. 
Check out the table below to see how each method interacts with a resource.

```java
@RequestMapping("/about", method = RequestMethod.GET)
```

…is equivalent to…

```java
@GetMapping("/about")
```

See below for a table of helper methods and the requests to which they map.

| HTTP Method Annotation |	Usage |
| --- | --- |
| `@GetMapping` | Used to specify GET requests to retrieve resources
| `@PostMapping` |	Used to specify POST requests to create new resources
| `@PutMapping` |	Used to specify PUT requests to update existing resources
| `@DeleteMapping` |	Used to specify DELETE requests to remove specific resources

## [Using Query Parameters](https://www.codecademy.com/courses/learn-spring/lessons/responding-to-requests-with-spring/exercises/using-query-parameters)

In the previous exercise, we discussed the use of helper methods to specify the HTTP method being used. 
GET requests are used to retrieve information from the server, while POST, PUT, or DELETE requests are used to make changes to resources on the server. 
In this exercise, we’ll discuss HOW those changes are transmitted from the user to the endpoint.

When users need to pass data to the server, the term we use to describe the process is called binding. 
The prime example of binding data from a user’s request to an endpoint occurs when a user needs to submit data. 
Imagine an application where you enter a book’s ISBN and the response returned is either a `yes`, indicating the book is available for checkout, 
or a `no`, indicating the book is not available. 
When the user submits their request, we need a way to bind their entry to the endpoint that will provide the response. 
Thankfully, there’s a Spring annotation for that!

`@RequestParam` is an annotation that can be used at the method parameter level. 
It allows us to parse query parameters and capture those parameters as method arguments. 
This is incredibly helpful because we can take values passed in from the HTTP request, parse them, 
and then bind the values to a controller method for further processing. 
We also have the option of defining a default value for the method argument in case a value is not received from the client.

In this example, let’s say the user submits their request for a book with 2 authors and a publishing year of 1995.

```
libraryapp.com/book?author_count=2&published_year=1995
```

The `author_count` and `published_year` values would map to the method parameters as follows:

```java
@GetMapping("/book")
public Book isBookAvailable(@RequestParam int author_count, @RequestParam int published_year) {
  return books.find(author_count, published_year);
}
```

## [Using Template Path Variables](https://www.codecademy.com/courses/learn-spring/lessons/responding-to-requests-with-spring/exercises/using-template-path-variables)

In the previous exercise, we discussed the use of `@RequestParam` to pass data from query parameters to a method. 
`@RequestParam` is perfect to use when we want to filter the results or return several resources. 
However, when we want to return more specific entities we can use the `@PathVariable` annotation.

`@PathVariable` maps template variables in the request URI directly to a method’s parameters. 
For example, we could define a template path

```
/books/{id}
```

and use the URI

```
localhost:4001/books/28937
```

to pass the path variable “28937” to a method’s `id` parameter. 
On the server side, we would have an endpoint that looks up books by ID as follows:

```java
@GetMapping("/{id}")
public Book isBookAvailable(@PathVariable int id)  {
  return book.findByID(id);
}
```

In the above example, use of the `@PathVariable` at the method parameter level allows us to take a variable received from the request URI 
and pass it into a method as a parameter. 
As a developer, this simple annotation affords us ample opportunities to process data from HTTP requests.

> We’ve seen two ways to capture parameters from a request URI. 
> `@RequestParam` captures the `id` included in the URI `/books?id=28937` 
> and `@PathVariable` captures the `id` included in the URI `/books/28937` as long as the path includes the `{id}` variable in `books/{id}`.







