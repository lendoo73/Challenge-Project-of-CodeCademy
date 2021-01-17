# Introduction to Flask-SQLAlchemy

## [Why have databases in your web applications?](https://www.codecademy.com/courses/learn-flask/lessons/flask-intro-sql-alchemy/exercises/databases-motivation-intro)

Web applications are often built around a lot of data that change frequently. 
The data is usually organized in entities related in some way. 
For example, entities such as users are related to products by the act of purchasing, music albums are related to a specific artist by authoring, users are related to other users by befriending, etc.

*Relational databases* offer robust and efficient data management. 
A usual relational database consists of tables that represent entities and/or relationships amongst entities. 
The attributes of entities are constrained (for example, NAME attribute is a string, and a user’s PASSWORD should not be empty). 
The way a database is organized in entities, attributes and relationships, without data being present, is called the database schema.

### Database schema design: A simple book club scenario

You want to create a personal book club application. 
Each month you pick a book your friends can review and rate. 
Your web app manages registered readers, the list of books you choose each month, and the ratings the readers write for those books. 
Moreover, you can show the annotations your friends made while reading the suggested books.

The schema for this problem is shown on bellow. 
Inspect the schema by following the instructions below.
![]()
