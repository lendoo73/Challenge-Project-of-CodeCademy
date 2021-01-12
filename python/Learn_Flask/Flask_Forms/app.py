from flask import Flask, render_template, request
from helper import recipes, types, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from forms import RecipeForm, CommentForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

@app.route("/", methods=["GET", "POST"])
def index():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
    new_id = len(recipes)+1
    recipes[new_id] = recipe_form.recipe.data
    types[new_id] = recipe_form.recipe_type.data
    descriptions[new_id] = recipe_form.description.data
    new_ingredients = recipe_form.ingredients.data
    new_instructions = recipe_form.instructions.data
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
    comments[new_id] = []
  return render_template("index.html", template_recipes=recipes, template_form=recipe_form)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm(csrf_enabled=False)
  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
  return render_template("recipe.html", template_recipe=recipes[id], template_type=types[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id], template_comments=comments[id], template_form=comment_form)

@app.route("/about")
def about():
  return render_template("about.html")
