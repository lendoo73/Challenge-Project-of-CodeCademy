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










