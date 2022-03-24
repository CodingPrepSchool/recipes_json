from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, SelectField, BooleanField
from wtforms.validators import DataRequired

class RecipieAdd(FlaskForm):
    name = StringField("Recipie Name: ", validators=[DataRequired()])
    ingrediants = TextAreaField("Ingredients: ", validators=[DataRequired()])
    instructions = TextAreaField("Instructions: ", validators=[DataRequired()])
    submit = SubmitField("Submit Recipie", validators=[DataRequired()])
