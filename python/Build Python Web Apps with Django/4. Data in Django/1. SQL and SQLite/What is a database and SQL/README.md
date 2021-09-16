# [What is a database and SQL](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-sql-and-sqlite/informationals/django-what-is-a-database-and-sql)

Before we continue our Djourney into models, we need to get a sense of databases — 
because databases are where we will ultimately store our models’ information and provide the structure for our projects’ and apps’ data.

As mentioned earlier in the introduction, [SQLite](https://www.sqlite.org/index.html) 
comes pre-installed with Python. 
We’ve also configured this database to work on our site for your convenience as you progress through Django lessons and projects.

The “Lite” part of SQLite’s name implies that it’s a lightweight database perfect for small, personal applications. 
The other portion “SQL“, pronounced like the word “sequel”, refers to the [Structured Query Language](https://en.wikipedia.org/wiki/SQL) 
which is used to interact with the database. 
But, as part of Django’s “swiss army knife” approach, developers can still interact with their databases even without knowing SQL 
because of Django’s [Object-Relational Mapping](https://en.wikipedia.org/wiki/Object–relational_mapping), 
or ORM. 
Simply speaking, we’re able to write Python code to interact with our SQLite database!
