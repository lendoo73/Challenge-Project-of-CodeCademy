# [Tourist Attractions](https://www.codecademy.com/courses/learn-flask/projects/tourist-attractions-app)

Whenever you travel it is fun to make a list of places you want to visit. 
The application you are about to create looks at making this list and organizing locations into 3 categories: 
* recommended places to visit, 
* decided places to visit 
* and places that have been visited. 

Within each category you will have the option to move a location up to the next category and also remove a location. 
Lastly, there is also the option to add new locations to any of the categories.

The application consists of 7 files, but we will only work on 3 of them. 
Let’s go over the files we won’t be working on:

* **/static/styles.css**: Basic css files to give the application some style and show off the benefits of template inheritance.
* **/templates/base.html**: Template header file that the main template file will inherit from.

* **data.csv**: Dummy data we will use to show of the functionality of the application as we build it.

* **location.py**: A module the application will rely on to add, modify and delete location data. 
Our application will instantiate a `Locations()` class from this module. 
With this instance we will rely on 3 methods:
* `add()`: Add a location to the data
* `moveup()`: Move the location up one category
* `delete()`: Delete a location from the data

The files we will be working with are as follows:

* **app.py**: The Flask application which consists of 3 routes:

  * `locations()`: The main route which will return return content associated with each category of location. 
  This route is also responsible for handling the changing of categories and deletion of locations.
  * `add_location()`: A form handling route which will process the add location form and then redirect back to the `locations()` route.
  * `index()`: This route is the same path as the `locations()` route but without a category variable. 
  It will automatically redirect to the recommended page of the `locations()` route.
* **/templates/locations.html**: Template file that displays the tourist attractions data.
* **forms.py**: A module that defines the form used in the application.

Now that we have described each file, feel free to walk through them yourself before you begin. 
This may help you understand what is happening as we accomplish each task.
