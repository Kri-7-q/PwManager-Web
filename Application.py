from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemyUserDatastore, Security
from AppForms.SecurityForms import ExtLoginForm, ExtRegisterUser
from Utility.DictObj import DictObj
from Utility.Credentials import Credentials

app = Flask('PwManager')
# ------------- Config -----------------------
conectionFile = Credentials.userHomePath() + '/.pwmanager'
credentials = Credentials.fromFile(conectionFile)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = credentials.connectionStringDB('postgresql')
# ---------------------------------------------
db = SQLAlchemy(app)
# Setup Flask-Security
from Database.Models import User, Role
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore, register_form=ExtRegisterUser, login_form=ExtLoginForm)
# ----------------------- Security forms processors ------------------------
@security.register_context_processor
def security_register_processor():
    return dict(pageValues=DictObj(header='Benutzer registrieren', login=True))

@security.login_context_processor
def security_login_processor():
    return dict(pageValues=DictObj(header='Anmelden'))

from Routing import PasswortManager