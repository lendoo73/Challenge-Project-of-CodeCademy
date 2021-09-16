#### MODELS AND DATABASES

# [What are Models](https://www.codecademy.com/paths/build-python-web-apps-with-django/tracks/data-in-django/modules/django-models-and-databases/lessons/django-models-and-databases/exercises/what-are-models)

We’ve seen firsthand how Django uses the [Model-Template-View (MTV) pattern](https://github.com/lendoo73/Challenge-Project-of-CodeCademy/tree/master/python/Build%20Python%20Web%20Apps%20with%20Django/4.%20Data%20in%20Django/2.%20Models%20and%20Databases/1.%20Modeling%20Real%20Life%20Objects) 
to bring our apps to life. 
This time around, we’ll focus on the model portion of this pattern which deals heavily with the data in our app — this means we’ll also dive into the database!

We can think of models as representations of everyday objects. These models maintain key characteristics/properties of the objects used in our app. Consider these three objects: a rose, a daisy, and a tulip. They are flowers. Flower could be our model name and correspond to the table name in our database. The model might have characteristics like petal_number and petal_color which correspond to field names (think of them as column headings) in our database.

Now imagine if we were creating a model for our users — trying to account for every single thing about a person would be almost impossible! Instead, we have to focus on the really important properties we want in our model that will later be stored as data in our database. How data gets organized in the database is known as a schema.

Also, notice that we mentioned models (plural) — in our apps, we’ll often work with more than just one. Therefore, we have to consider how models interact with each other and what relationships exist. The persistence of model data and how different models interact will drive the flow of our app!

In this lesson, we’ll go through:

How to think through schemas
Creating and customizing models
Connecting the Models with the Database
With that information out of the way, let’s Django!
