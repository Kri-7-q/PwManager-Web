from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security
from AppForms.SecurityForms import ExtLoginForm, ExtRegisterUser
from Utility.DictObj import DictObj

app = Flask('PwManager')
# ------------- Config -----------------------
app.config.from_object('config')
# ---------------------------------------------
db = SQLAlchemy(app)
# Setup Flask-Security
from Database.Models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=ExtRegisterUser, login_form=ExtLoginForm)
# ----------------------- Security forms processors ------------------------
@security.register_context_processor
def security_register_processor():
    return dict(pageValues=DictObj(header='Benutzer registrieren'))

@security.login_context_processor
def security_login_processor():
    return dict(pageValues=DictObj(header='Anmelden'))

from Routing import PasswortManager