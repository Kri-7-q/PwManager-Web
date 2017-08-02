from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired
from Utility.Validators import integerValidator
from Utility.DictObj import DictObj

class EditForm(FlaskForm):
    id = IntegerField('id', validators=[integerValidator])
    provider = StringField('Anbieter', validators=[DataRequired()])
    username = StringField('Benutzername', validators=[DataRequired()])
    password = StringField('Passwort', validators=[DataRequired()])
    passwordlength = IntegerField('Passwortlänge', validators=[DataRequired(), integerValidator])
    definedcharacter = StringField('Erlaubte Zeichen')
    question = StringField('Sicherheitsfrage')
    answer = StringField('Antwort')

    # Get form data as a DictObj object.
    def getDict(self):
        return DictObj(id=int(self.id.data), provider=self.provider.data, username=self.username.data,
                       password=self.password.data, passwordlength=self.passwordlength.data,
                       definedcharacter=self.definedcharacter.data, question=self.question.data,
                       answer=self.answer.data)
