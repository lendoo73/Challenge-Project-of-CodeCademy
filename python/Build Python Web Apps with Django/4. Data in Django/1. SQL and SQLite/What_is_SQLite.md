# [What is SQLite](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-sql-and-sqlite/articles/django-what-is-sqlite)

Learn about the SQLite database which comes pre-configured for Django.

In this article, we will be exploring the extremely prevalent database engine called [SQLite](https://www.sqlite.org/index.html). 
We will describe what it does and its main uses. 
While you don’t need to learn SQL for Django, it’s helpful to get an overview of what it does and how it works with SQLite.

## What is SQLite?

SQLite is a database engine. 
It is software that allows users to interact with a relational database. 
In SQLite, a database is stored in a single file — a trait that distinguishes it from other database engines. 
This fact allows for a great deal of accessibility: copying a database is no more complicated than copying the file that stores the data, 
sharing a database can mean sending an email attachment.

## Drawbacks to SQLite

SQLite’s signature portability unfortunately makes it a poor choice when many different users are updating the table at the same time 
(to maintain integrity of data, only one user can write to the file at a time). 
It also may require some more work to ensure the security of private data due to the same features that make SQLite accessible. 
Furthermore, SQLite does not offer the same exact functionality as many other database systems, limiting some advanced features other relational database systems offer. 
Lastly, SQLite does not validate data types. 
Many other database software would reject data that does not conform to a table’s schema, how a table’s data is organized. 
However, SQLite allows users to store data of any type into any column.

SQLite creates schemas, which constrain the type of data in each column, but it does not enforce them. 
The example below shows that the `id` column expects to store integers, the `name` column expects to store text, and the `age` column expects to store integers:
```sql
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
);
```
However, SQLite will not reject values of the wrong type. We could accidentally insert the wrong data types in the columns. Storing different data types in the same column is a bad habit that can lead to errors that are difficult to fix, so it’s important to be strict about your schema even though SQLite will not enforce it.

Uses for SQLite
Even considering the drawbacks, the benefits of being able to access and manipulate a database without involving a server application are huge. SQLite is used worldwide for testing, development, and in any other scenario where it makes sense for the database to be on the same disk as the application code. SQLite’s maintainers consider it to be among the most replicated pieces of software in the world.

Conclusion
You now know about the database software that comes pre-configured for Django. Congratulations! For more info, check our article on other Relational Database Management Systems.
