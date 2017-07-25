from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('PwManager')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://christian:kri-7-q@localhost:3306/pwmanager'
db = SQLAlchemy(app)

from Routing import PasswortManager