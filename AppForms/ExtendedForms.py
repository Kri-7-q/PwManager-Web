from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import IntegerField
from wtforms.validators import DataRequired
from Utility.Validators import integerValidator
from Database.Models import modelAttribute as label

class EditForm(FlaskForm):
    id = IntegerField(label.id, validators=[integerValidator])
    provider = StringField(label.provider, validators=[DataRequired()])
    username = StringField(label.username, validators=[DataRequired()])
    password = StringField(label.password, validators=[DataRequired()])
    passwordlength = IntegerField(label.passwordlength, validators=[DataRequired(), integerValidator])
    definedcharacter = StringField(label.definedcharacter)
    question = StringField(label.question)
    answer = StringField(label.answer)


class GeneratePwdForm(FlaskForm):
    lenght = IntegerField('Passwortlänge', validators=[integerValidator])
    password = PasswordField('Passwort', validators=[DataRequired()])
    definedcharacter = StringField('Erlaubte Zeichen', validators=[DataRequired()])