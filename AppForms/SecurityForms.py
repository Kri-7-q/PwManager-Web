from flask_security.forms import RegisterForm, LoginForm, unique_user_email, email_validator, email_required
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, EqualTo
from wtforms.fields.html5 import EmailField

class ExtLoginForm(LoginForm):
    email = StringField('Benutzername', validators=[InputRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=50)])
    submit = SubmitField('Anmelden')


class ExtRegisterUser(RegisterForm):
    name = StringField('Benutzername', validators=[InputRequired(), Length(min=3, max=50), unique_user_email])
    email = EmailField('eMail', validators=[email_validator, email_required, unique_user_email])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=50)])
    password_confirm = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=50),
                                                             EqualTo('password', message='Passwort wurde falsch wiederholt.')])
    submit = SubmitField('Registrieren')
