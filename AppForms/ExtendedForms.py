from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from Utility.Validators import integerValidator

class EditForm(FlaskForm):
    provider = StringField('Anbieter', validators=[DataRequired()])
    username = StringField('Benutzername', validators=[DataRequired()])
    password = StringField('Passwort', validators=[DataRequired()])
    passwordlength = IntegerField('Passwortlänge', validators=[DataRequired(), integerValidator])
    definedcharacter = StringField('Erlaubte Zeichen')
    question = StringField('Sicherheitsfrage')
    answer = StringField('Antwort')
