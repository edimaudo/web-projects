from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class IdeaForm(FlaskForm):
    idea_name = StringField('idea_name', validators=[DataRequired()])
    idea_description = StringField('idea_description', validators=[DataRequired()])
