#### MODELS AND DATABASES

# [Migrations - migrate](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/migrations-migrate)

With our migration file set up, it’s time to use the code in our file to make changes to our database.

The command to execute at the terminal would be:
```
python3 manage.py migrate
```
Like `makemigrations`, if our project supports multiple apps, we can pass in the particular app name to the [`migrate` command](https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-migrate) 
as well. 
For example:
```
python3 manage.py migrate garden
```
Where `garden` is the name of our app. 
We should see some output like:
```
Operations to perform:
  Apply all migrations: gardens
Running migrations:
  Rendering model states... DONE
  Applying garden.0001_initial... OK
```
After executing the `migrate` command, our database is set up! 
Under the hood, Django is [handling the SQL commands](https://docs.djangoproject.com/en/3.1/ref/django-admin/#django-admin-sqlmigrate) 
needed to make this migration happen — however, that’s beyond this lesson’s scope.

If we need to reverse a migration, Django also makes this possible by specifying the migration we want to revert back to:
```py
python3 manage.py migrate <migration_name>
```
Where we replace `<migration_name>` with the name of the migration like `0001`. 
Then the database’s schema reverts back to the model from our `0001` migration!

However, in some cases, migrations cannot be unapplied like if we dropped a table in a previous migration. 
In such cases, we’ll get an `IrreversibleError`. 
Check out Django’s [documentation](https://docs.djangoproject.com/en/3.1/topics/migrations/#reversing-migrations) 
for more information.
