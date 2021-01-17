from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField
from wtforms.validators import DataRequired


class FieldsRequiredForm(FlaskForm):
    """Require radio fields to have content. This works around the bug that WTForms radio fields don't honor the `DataRequired` or `InputRequired` validators."""
    class Meta:
        def render_field(self, field, render_kw):
            if field.type == "_Option":
                render_kw.setdefault("required", True)
            return super().render_field(field, render_kw)


categories = [
    ("recommended", "Recommended"), 
    ("tovisit", "Places To Go"), 
    ("visited", "Visited!!!")
]

# Create Form Here


class AddLocationForm(FieldsRequiredForm):
    name = StringField(
        "Location Name",
        validators=[DataRequired()]
    )
    description = TextAreaField(
        "Location Description",
        validators=[DataRequired()]
    )
    category = RadioField(
        "Category",
        choices=categories
    )
    submit = SubmitField("Add Location")
