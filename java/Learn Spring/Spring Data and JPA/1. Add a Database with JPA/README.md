# Add a Database with JPA

## [What is Spring Data JPA?](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/what-is-spring-data-jpa)

Spring Data JPA is a library for Spring that helps to integrate a database into your REST API.

In this lesson, we will create an application that will help a botanist keep track of their inventory of plants.

Our database will store information about different plants, how many of them the botanist has, and how often they need to be watered to stay healthy.

Your Spring Boot application will wrap around this database, helping us manage the botanist’s inventory with simple REST calls.

## [Connecting to a Database](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/connecting-to-a-database)

To connect to an embedded H2 database using Spring Data JPA, we’ll need to update your application’s properties. 
Spring uses a **properties file** to store information that your application depends on. 
The type of information that is typically stored inside properties files includes:

* the database URL
* the amount of logs your application should produce
* the “port” your application runs on

When our Spring Boot application starts, it will check the properties file, located at **src/main/resources/application.properties**, 
for any information that it might require to configure our application correctly.

## [Create a Model](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/create-a-model)

As mentioned earlier, Spring Data JPA is an abstraction layer that allows us to interact with objects in your code rather than write SQL queries.

These objects, in this context, are referred to as models (or entities). 
Typically, we write Java classes and use annotations to identify them as models to Spring Data JPA. 
Then, Spring Data JPA sends instructions to the Hibernate ORM to execute the correct SQL statements 
depending on the methods that we’ve called on our model and the annotations we’ve put on its fields.

You can imagine that a model corresponds to a database table, and a field in a model corresponds to a column in that table. 
An application developer will use annotations to indicate how the model name and field names translate to the underlying table 
name and column names, respectively. 
To gain a better understanding of how we can create a model, and use annotations to map it to the underlying database relation/table, 
let’s analyze an example.

Below, you’ll see a **P**lain **O**ld **J**ava **O**bject (a POJO) that represents a person, storing their attributes as fields of our POJO.
```java
// Person, a Plain Old Java Object (POJO), that we use to represent a person.
public class Person {
 
  // An ID to uniquely identify the person we are storing in our db
  private Integer id;
 
  private String name;
  private Integer age;
  private String eyeColor;
}
```

Now that we have a baseline representation of what a Person is and what we wish to store about them, 
we can add annotations from JPA that help define how our Java object will map to a database relation.
```java
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.Column;
import javax.persistence.Table;
 
@Entity
@Table(name="PEOPLE")
public class Person {
 
    @Id
    @GeneratedValue
    private Integer id;
 
    @Column(name="NAME")
    private String name;
 
    @Column(name="AGE")
    private Integer age;
 
    @Column(name="EYE_COLOR")
    private String eyeColor;
 
}
```

In the example, we start with importing all of the annotations that we’ll need. 
These annotations come from the JPA library, which comes along with the `spring-boot-starter-data-jpa dependency`.

Then, we add in all the required annotations that define the translation between our POJO and our database relation:

* **`@Entity`**: tells the ORM that this model will be used to represent a table or relation in our database
* **`@Table`**: tells the ORM what table name in the underlying database that this model corresponds to. 
Here, it is used to say that the `Person` entity represents a single entry in the `"PEOPLE"` table of the underlying database.
* **`@Id`**: tells the ORM that this field (`id`) will be used to uniquely identify a single entry in our `"PEOPLE"` relation
* **`@GeneratedValue`**: tells the ORM that the developer will not be supplying the value for this field themselves. 
Instead, it should be “auto-generated” by the database. 
Typically, an `@Id` field for an entity will be auto-generated in this way, 
so that we can leverage the database to guarantee that the ID will always be unique.
* **`@Column`**: tells the ORM what column in the underlying relation that the annotated field corresponds to. 
For example, the `eyeColor` field of our entity corresponds to the `"EYE_COLOR"` column in the `"PEOPLE"` relation.

There are many more annotations that JPA provides to help define more complex relationships between a model and its underlying relation in the database. 
You can read more about them [here](https://docs.oracle.com/javaee/7/api/javax/persistence/package-summary.html) 
under the Annotation Types Summary heading. 
However, the ones from the example above should cover the majority of common use cases.

When the ORM interacts with your model, it depends on “getter” and “setter” methods that have been appropriately named based on the fields. 
For the `Person` class, we would additionally need to add getter and setter methods 
for every field to ensure that the ORM can access and modify fields in the model as required.

We won’t write out the whole class again, but you can imagine that the `age` field, for example, would have a getter and setter like this:
```java
@Column(name="AGE")
private Integer age;
 
public Integer getAge() {
  return this.age;
}
 
public void setAge(Integer age) {
  this.age = age;
}
```

Now that you are equipped to define models and use JPA annotations to map them to relations, 
you can apply these skills for the plant management application we are creating for the botanist!

## [Create a Repository](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/create-a-repository)

Now that we have learned how data models are defined, the next step is to determine how to use the model to interact with the database. 
Spring Data JPA uses repositories to accomplish this. 
A repository is a data access and manipulation layer that wraps around your data model. 
A repository will come with methods to call on instances of your data model like `.save()`, or `.findAll()`, or .`findById()`, 
enabling a no-code solution to interacting with a data model in a Spring Boot application.

When developers build APIs that interact with or manage an underlying data model, there are usually some common functionalities that they want to enable. 
An API that manages a data model should be able to **C**reate, **R**ead, **U**pdate, and **D**elete instances of the model. 
For this reason, these kinds of APIs are called **CRUD API**s.

Since this kind of functionality is so common, Spring Data JPA comes with a special kind of repository interface 
that gives you full CRUD functionality for your model. 
To use it, an application developer simply imports the repository interface, tells it what model it should wrap around, and it is good to use!

Here’s an example of how the `CrudRepository` interface would work with the `Person` class from the previous exercise:
```java
import org.springframework.data.repository.CrudRepository;
 
import com.codecademy.people.entities.Person;
 
// creating an extension of the CrudRepository that can manage our Person model
public interface PersonRepository extends CrudRepository<Person, Integer> {
  // no method declarations are required! }
```

In this example, we create a new interface that extends the `CrudRepository`, and parameterize it with our `Person` model 
and the type of its ID field, `Integer`.

> The angle brackets (< >) are a special kind of syntax used in Java to provide more specific type information to a class, using 
> [type parameters](https://docs.oracle.com/javase/tutorial/java/generics/types.html). 
> You may have seen these used when we have a `List` of things in Java, like `List<Integer>`. 
> In this example, the first type parameter is used to ensure that our `PersonRepository` 
> knows it is responsible for managing instances of the `Person` object. 
> The second type parameter is used to tell the repository the type of the `ID` field, which enables methods like `.findById`.

Some methods that the `CrudRepository` interface offers us to enable CRUD functionality are:

* **`.findById(Integer id)`**: allows you to query the database to find an instance of your model by its ID field
* **`.findAll()`**: allows you to retrieve ALL the entries in the database for a given model
* **`.save(Person p)`**: allows you to create AND modify instances of your model in the database
* **`.delete(Person p)`**: allows you to delete instances of your model from the database

In this exercise, you’ll use the `CrudRepository` interface to enable CRUD operations for the plant management application.

## [Connect Your Repository to a Controller](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/connect-your-repository-to-a-controller)

The repository interfaces provided by Spring Data JPA, such as `CrudRepository`, are very powerful for managing data without having to write too much code. 
However, they are not of much use without a way for an end user of your API to interact with them.

When a user wishes to interact with your API, they do so by making **REST** calls to a `RestController`. 
A `RestController` is used as the layer of the application that takes requests from the user and accordingly sends commands to the repository 
or data access layer to accomplish what task the user requested in their REST call.

The repository must be a dependency of the controller, and you can make the repository bean available to the controller class using *dependency injection*.

Since the extension of the `CrudRepository` will be used in the “Spring context,” it is implicitly a bean.

To make a bean available to a class that depends on it, you can simply add it as a field of the class and include it in the constructor. 
Spring Boot will automatically “wire” in the dependency when it discovers the dependency in the Spring context. 
For the `PersonRepository` example, we could have a `PersonController` that looks like:

```java
import org.springframework.web.bind.annotation.RestController;
 
import com.codecademy.people.repositories.PersonRepository;
 
@RestController
public class PersonController {
  private final PersonRepository personRepository;
 
  public PersonController(final PersonRepository personRepository) {
    this.personRepository = personRepository;
  }
 
  // ... all REST endpoint mappings
}
```

To make the `PersonRepository` available to the `PersonController` as a dependency, all that had to be done was:

* Import the `PersonRepository` from the correct package
* Add the `PersonRepository` as a field in the `PersonController` class
* Add the `PersonRepository` to the constructor and assign it to the field appropriately

In this exercise, you’ll do the same to enable the `PlantRepository` to be used by the `PlantController` class.

## [Make Queries to Your Database: findAll](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/make-queries-to-your-database-findall)

Now that you can communicate between your controller and your data access layer, you’ve bridged the gap between an end user of your API and the database.

One of the fastest ways to test this functionality is by implementing some `GET` endpoints in the controller. 
The `GET` request should be used to retrieve information out of your database, 
so it makes sense that a `GET` request should trigger repository methods like `.findAll()` or `.findById(Integer id)`.

Continuing the example of the `Person` model, our `PersonController` may include some `@GetMappings` to accomplish this:

```java
import java.lang.Iterable;
import java.util.Optional;
 
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.GetMapping;
 
import com.codecademy.people.entities.Person;
import com.codecademy.people.repositories.PersonRepository;
 
@RestController
public class PersonController {
 
  private final PersonRepository personRepository;
 
  public PersonController(final PersonRepository personRepository) {
    this.personRepository = personRepository;
  }
 
  @GetMapping("/people")
  public Iterable<Person> getAllPeople() {
    return this.personRepository.findAll();
  }
 
  @GetMapping("/people/{id}")
  public Optional<Person> getPersonById(@PathVariable("id") Integer id) {
    return this.personRepository.findById(id);
  }
}
```

In this example, the `"/people"` endpoint of this API will fetch all `Person` entries from the `PersonRepository` 
using the `.findAll()` method offered by the `CrudRepository`. 
It returns an `Iterable`, which is just a simplified interface for a collection in Java. 
Note that the `Iterable` has a type parameter, `Person`.

You would test this functionality by making a `GET` request with `curl`, or even navigating to that endpoint in a web browser!

```
curl localhost:4001/people
 
# [
#   {
#     "id": 1,
#     "eyeColor": "green",
#     "name": "Tammy Green",
#     "age": 31
#   },
#   {
#     "id": 2,
#     "eyeColor": "hazel",
#     "name": "Rashid Jordan",
#     "age": 14
#   },
#   {
#     "id": 3,
#     "eyeColor": "brown",
#     "name": "Aneeqa Kumar",
#     "age": 23
#   }
# ]
```

## [Make Queries to Your Database: findById](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/make-queries-to-your-database-findbyid)

Rather than get all items, our API users may want to find a specific entity in the database. 
For this kind of request, we can use `CrudRepository` methods like `.findById(Integer id)`.

Continuing the example of the `Person` model, we would add this endpoint to our `PersonController`:

```java
import java.util.Optional;
// Other imports and class scaffolding omitted
 
@GetMapping("/people/{id}")
public Optional<Person> getPersonById(@PathVariable("id") Integer id) {
  return this.personRepository.findById(id);
}
```

The endpoint, `"/people/{id}"`, uses a path parameter so that the user of the API can pass in the `id` in the URL in their request. 
The responsibility of the controller class is to extract this `id` from the request and pass it into the `.findById` method in the repository.

Note that this method returns an `Optional<Person>`. 
This is because the user may pass an ID that does not exist in the database. 
The `Optional` type from Java will allow the response to gracefully return `null` in the response body 
if the `id` supplied could not be found in the database.

A request to this endpoint might look like:

```
# Request for an ID that exists
curl localhost:4001/people/3
 
# {
#   "id": 3,
#   "eyeColor": "brown",
#   "name": "Aneeqa Kumar",
#   "age": 23
# }
 
 
# Request for an ID that does not exist
curl localhost:4001/people/50
 
# null
```

# [Create a New Database Entry](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/create-a-new-database-entry)

Conventionally, a `GET` request is used when you wish to `GET` information from the database. 
Similarly, a `POST` request is used when we wish to create new information in the database.

With Spring Data JPA’s `CrudRepository`, you can use the `.save()` method to create records in the database. 
The `.save()` method accepts your model as a parameter, and uses all the annotations you added to indicate the columns as its basis 
when it uses the ORM to create the underlying SQL `INSERT` statement.

Once again, we’ll refer to the `Person` example:

```java
@PostMapping("/people")
public Person createNewPerson(@RequestBody Person person) {
  Person newPerson = this.personRepository.save(person);
  return newPerson;
}
```

In this example, the end user of the API would pass in a `Person` using the body of their `POST` request. 
To save this person to our database, we use the `.save` method from the `PersonRepository`. 
The `.save` method returns a `Person` as well, and the only difference between this `newPerson` and the original person passed by the user is 
that the `newPerson` will have an `id` field, generated by means of the `@GeneratedValue` annotation from the model definition.

Lastly, this `newPerson` is returned in the response body, so that the end user can know the ID 
that was assigned to the new entry they created in the database.

Now, let’s do something similar for our plants application.


## [Update a Database Entry](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/update-a-database-entry)

The `.save` method from the `CrudRepository` interface can be used both for creating new entries in the database as well as updating existing entries.

A common flow is to fetch an entry from the database by its ID, update some attribute of the entry, and then call `.save` again to persist the change.

Like how `GET` requests are used for reading entries from the database, and `POST` requests are used for creating new entries in the database, 
convention dictates that you should use `PUT` requests to update entries in the database.

Here’s what a `PUT` endpoint to update a `Person` would look like:
```java
@PutMapping("/plants/{id}")
public Person updatePerson(@PathVariable("id") Integer id, @RequestBody Person p) {
  Optional<Person> personToUpdateOptional = this.personRepository.findById(id);
  if (!personToUpdateOptional.isPresent()) {
    return null;
  }
 
  // Since isPresent() was true, we can .get() the Person object out of the Optional
  Person personToUpdate = personToUpdateOptional.get();
 
  if (p.getName() != null) {
    personToUpdate.setName(p.getName());
  }
  if (p.getAge() != null) {
    personToUpdate.setAge(p.getAge());
  }
  if (p.getEyeColor() != null) {
    personToUpdate.setEyeColor(p.getEyeColor());
  }
 
  Person updatedPerson = this.personRepository.save(personToUpdate);
  return updatedPerson;
}
```

In this example, the `updatePerson` method takes an `Integer id` as path parameter and a `Person p` as the request body.

The `id` path parameter is used in the call to `this.personRepository.findById` to find the `Person` entry in the `PEOPLE` table that we wish to update.

We first check if the `id` existed in the database with the `.isPresent()` method on the `Optional<Person> personToUpdateOptional`. 
If it was not present, that meant the `id` did NOT exist in the database, so the method terminates early by returning `null` to the response body.

Otherwise, if `.isPresent()` was NOT false, we can proceed to `.get()` the underlying `Person` object out of the `Optional` 
and use it for the rest of the method.

The `Person` object passed in the request body is used to store the new field values that should be used to update the targeted entry. 
It does not need to have ALL the fields that a `Person` has. 
When Spring Boot (via Jackson) converts the request body to a `Person` object, it simply sets any fields that are missing to `null`. 
Because of this, we are able to use a single endpoint to update any field of the `Person`. 
We can use `if` statements to update a field of the target database entry ONLY IF the corresponding field in the request body object was not null.

Lastly, we call the `CrudRepository` `.save` method to persist the changes that we made to the person. 
We return the output of the `.save` method (`updatedPerson`) to the user in the response body, so that they can see how the target entry was updated.

## [Delete a Database Entry](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/delete-a-database-entry)

So far, you have:
* Used a `POST` endpoint to Create a database entry
* Used a `GET` endpoint to Read database entries
* Used a `PUT` endpoint to Update a database entry

Sounds like you’re just one capability away from having a full-fledged **CRUD** application!

Implementing a `DELETE` endpoint that can **D**elete a database entry is straightforward. 
The `CrudRepository` offers a delete method that accepts the instance of the model that you wish to delete. 
For the `Person` example, this looks like:
```java
@DeleteMapping("/people/{id}")
public Person deletePerson(@PathVariable("id") Integer id) {
  Optional<Person> personToDeleteOptional = this.personRepository.findById(id);
  if (!personToDeleteOptional.isPresent()) {
    return null;
  }
  Person personToDelete = personToDeleteOptional.get();
  this.personRepository.delete(personToDelete);
  return personToDelete;
}
```

Notice that the `.delete` method differs slightly from the `.save` method that we have seen, in that it does not return anything. 
Instead of depending on the output of the `.delete` method to give a response back to the user of the API, 
we capture the object before it is deleted using `.findById`, and return that object to the user after the `personToDelete` has been deleted.

As was the case for getting and updating a plant by ID, we should use the `Optional` methods to check to see if the `id` supplied was valid, 
and terminate the method early by returning `null` if it was not present in the database.

## [Review](https://www.codecademy.com/courses/learn-spring/lessons/add-a-database-with-jpa/exercises/spring-data-jpa-i-review)

Congratulations! You’ve completed a **CRUD** application end-to-end with *Spring Boot* and *Spring Data JPA*. Your application can:

* **C**reate plants in the database by making **POST** requests and the `.save` method of `CrudRepository`
* **R**ead plants in the database by making `GET` requests and the `.findAll()` and `.findById()` methods of `CrudRepository`
* **U**pdate plants in the database by using getters and setters to check and modify fields in the `Plant` entity, and the `.save` method of `CrudRepository`
* **D**elete plants in the database by using the `.delete` method of the `CrudRepository`.

With this knowledge, you should be able to create any **CRUD** application with *Spring Boot* for any data model. 
So lace your boots and spring into action!

Play around with your Plants application! 
Try using `curl` to stress test all of your endpoints and ensure you haven’t introduced any bugs unintentionally.

If it makes it easier to read, you can “pipe” the output of `curl` into `json_pp` like below:
```
curl localhost:4001/plants | json_pp
```
