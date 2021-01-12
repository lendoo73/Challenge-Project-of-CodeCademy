
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired

class RecipeForm(FlaskForm):
  recipe_categories = [("Breakfast","Breakfast"), ("Lunch","Lunch"), ("Dinner","Dinner")]
  recipe =  StringField("Recipe", validators=[DataRequired()])
  recipe_type = RadioField("Type", choices=recipe_categories)
  description = StringField("Description")
  ingredients = TextAreaField("Ingredients")
  instructions = TextAreaField("Instructions")
  submit = SubmitField("Add Recipe")

class CommentForm(FlaskForm):
  comment =  StringField("Comment", validators=[DataRequired()])
  submit = SubmitField("Add Comment")
