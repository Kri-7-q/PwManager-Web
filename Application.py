from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('PwManager')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://christian:kri-7-q@localhost:3306/pwmanager'
app.config['SECRET_KEY'] = b'tb\xa9\x07:\xb6\x04=Q]\xbaJ\xdbC\xe1\x18}Wk\xe5g\x11\xcb\x8b\xa5\x17"R[\x80l\r'
db = SQLAlchemy(app)

from Routing import PasswortManager