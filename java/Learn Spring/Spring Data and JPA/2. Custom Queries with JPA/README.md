# Custom Queries with JPA

## [Introduction](https://www.codecademy.com/courses/learn-spring/lessons/spring-custom-queries-with-jpa/exercises/introduction-custom-queries)

Now that you have completed implementing basic **CRUD** functionality, it’s natural to ask: What’s next?

Spring Data JPA’s `CrudRepository` interface is even more powerful than basic `findAll` and `findById` queries. 
We can add custom filter queries to our extension of the `CrudRepository` simply by adding a properly formatted method name to the interface. 
You don’t even have to implement the method!

For example, say we have a `Person` entity with a `String eyeColor` field, and we wish to query people in the database that have a certain eyeColor. 
We can simply add a method declaration to the `PersonRepository`:
```java
package com.codecademy.people.repositories;
 
import java.util.List;
import org.springframework.data.repository.CrudRepository;
import com.codecademy.people.entities.Person;
 
public interface PersonRepository extends CrudRepository<Person, Integer> {
  // this declaration is all we need!
  List<Person> findByEyeColor(String eyeColor); 
}
```

Based on how the method is named (`findByEyeColor`), Spring Data JPA will automatically generate the “implementation” of the method 
when your application is compiled. 
This capability is extremely powerful, as it allows developers to create complex queries without even writing the code for them!

To use our newly defined `findByEyeColor` method, we could implement a new `GET` `/people/search endpoint` in the `PersonController`.
```java
@GetMapping("/people/search")
public List<Person> searchPeople(
  @RequestParam(name = "eyeColor", required = false) String eyeColor
) {
  if (eyeColor != null) {
    return this.personRepository.findByEyeColor(eyeColor)
  } else {
    return new ArrayList<>();
  }
}
```

In the endpoint implementation above, we use query parameters with the `@RequestParam` annotation. 
This is the common convention in REST APIs when passing in parameters used for searching or filtering. 
A request to this endpoint would look like:
```
curl localhost:4001/people/search?eyeColor=brown
 
# [
#   {
#     "id": 3,
#     "eyeColor": "brown",
#     "name": "Aneeqa Kumar",
#     "age": 23
#   }
# ]
```

Take note of these two items; we’ll explain them in the following exercises:

1. The naming of the method declarations is extremely important here. 
The rules for the method names are detailed in the 
[Spring documentation here](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#jpa.query-methods.query-creation).

2. We added `required = false` inside the `@RequestParam` annotation.

## [Advanced Custom Queries](https://www.codecademy.com/courses/learn-spring/lessons/spring-custom-queries-with-jpa/exercises/advanced-custom-queries)

Notice that we added `required = false` inside our previous `@RequestParam` annotation. 
This allows us to optionally add more query parameters if the user would like to search by a different field value instead. 
For example, we could extend the `PersonRepository` interface with another method:
```java
List<Person> findByAgeLessThan(Integer age);
```

and update the `searchPeople` method accordingly:

```java
@GetMapping("/people/search")
public List<Person> searchPeople(
  @RequestParam(name = "eyeColor", required = false) String eyeColor,
  @RequestParam(name = "maxAge", required = false) Integer maxAge 
) {
  if (eyeColor != null) {
    return this.personRepository.findByEyeColor(eyeColor)
  } else if (maxAge != null) {
    return this.personRepository.findByAgeLessThan(maxAge);
  } else {
    return new ArrayList<>();
  }
}
```

You can get even more advanced using **And** queries, so that you could query the `PEOPLE` table by both eyeColor and maxAge at the same time. 
The new method declaration in the interface would look like:
```java
List<Person> findByEyeColorAndAgeLessThan(String eyeColor, Integer age);
```

The updated `searchPeople` method would look like:
```java
@GetMapping("/people/search")
public List<Person> searchPeople(
  @RequestParam(name = "eyeColor", required = false) String eyeColor,
  @RequestParam(name = "maxAge", required = false) Integer maxAge 
) {
  if (eyeColor != null && maxAge != null) {
    return this.personRepository.findByEyeColorAndAgeLessThan(eyeColor, maxAge);
  } else if (eyeColor != null) {
    return this.personRepository.findByEyeColor(eyeColor);
  } else if (maxAge != null) {
    return this.personRepository.findByAgeLessThan(maxAge);
  } else {
    return new ArrayList<>();
  }
}
```

As you can tell by now, Spring Data JPA’s `CrudRepository` is a lot more powerful than it initially lets on!

The naming of the method declarations is extremely important here. 
The rules for the method names are detailed in the [Spring documentation here](https://docs.spring.io/spring-data/jpa/docs/current/reference/html/#jpa.query-methods.query-creation).

Review the rules before proceeding to implement some custom query methods for the plant application in this exercise.

`curl` CLI queries:
```
curl "localhost:4001/plants/search?hasFruit=false&maxQuantity=20"
 
curl "localhost:4001/plants/search?hasFruit=false"
 
curl "localhost:4001/plants/search?hasFruit=true"
 
curl "localhost:4001/plants/search?hasFruit=true&maxQuantity=10"
 
curl "localhost:4001/plants/search?maxQuantity=10"
```






