from flask import Flask, render_template, request, redirect, url_for
from locations import Locations
from forms import AddLocationForm

app = Flask(__name__)
# this is necessary to protect against a Cross-Site Request Forgery attack:
app.config['SECRET_KEY'] = 'SECRET_PROJECT'

visit = Locations()
categories = {
    "recommended": "Recommended",
    "tovisit": "Places To Go", 
    "visited": "Visited!!!", 
}

UP_ACTION = "\u2197"
DEL_ACTION = "X"


@app.route("/<category>", methods=["GET", "POST"])
def locations(category):
    # Check the request for form data and process
    if request.method == "POST":
        [(name, action)] = request.form.items()

        if action == UP_ACTION:
            visit.moveup(name)
        elif action == DEL_ACTION:
            visit.delete(name)

    locations = visit.get_list_by_category(category)
    # Return the main template with variables
    return render_template(
        "locations.html",
        category=category,
        categories=categories,
        locations=locations,
        add_location=AddLocationForm()
    )


@app.route("/add_location", methods=["POST"])
def add_location():
    # Validate and collect the form data
    add_form = AddLocationForm()
    category = add_form.category.data

    if add_form.validate_on_submit():
        name = add_form.name.data
        description = add_form.description.data
        print("name", name)
        print("description", description)
        print("category", category)
        visit.add(name, description, category)
    # Redirect to locations route function
    return redirect(url_for(
        "locations",
        _external=True,
        category=category,
        _scheme="http"
    ))


@app.route("/")
def index():

    # Redirect to locations route function
    return redirect(url_for(
        "locations",
        category="recommended",
        _external=True,
        _scheme="http"
    ))
