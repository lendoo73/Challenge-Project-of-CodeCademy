# Databases in Flask - Reading, Updating and Deleting

## [Interacting with a Database](https://www.codecademy.com/courses/learn-flask/lessons/flask-read-update-delete-database/exercises/interacting-with-database)

Your database has a number of readers who subscribed to your book club and some books you already assigned to be read. 
Also some of your readers wrote reviews about the books and some of them might have some annotations made while reading their books on an eReader. 
The schema representing the database:
![database shema](images/books-schema.webp)

What can you do with the database?

Say you want to list all the books you suggested or list all the subscribed readers. Or let each subscriber see only the reviews they wrote. When new people subscribe to your web service, you need to add them to your database, or when they unsubscribe delete them. If you made a mistake in changing your database, you probably want to undo the changes or ‘rollback’ to the previous correct state. When your subscribers change their e-mail, you need to update your database. Or you need to filter out the books your club read in the year 2019 and only calculate average ratings of those. These are all the most common interactions with a database, and in this lesson, you will learn how to perform them in Flask-SQLAlchemy.

Throughout this exercise we will provide you with a database containing some entries for you to query, but you will learn how to add more entries, and remove some, on the way.

Can’t wait? Let’s go.
