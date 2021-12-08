from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField("Task Description", validators=[DataRequired()]) # The form cannot be submitted without data in the relevant field.
    submit = SubmitField("Add Task") # Add Task is what will be shown on the button