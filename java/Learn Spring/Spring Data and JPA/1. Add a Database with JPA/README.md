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
