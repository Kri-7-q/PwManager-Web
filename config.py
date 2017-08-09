# Flask
DEBUG = True
HOST = 'localhost'
PORT = 5000
# SQL Alchemy
#SQLALCHEMY_DATABASE_URI = 'postgresql://christian:kri-7-q@localhost:3306/pwmanager'
# Security
SECRET_KEY = b'tb\xa9\x07:\xb6\x04=Q]\xbaJ\xdbC\xe1\x18}Wk\xe5g\x11\xcb\x8b\xa5\x17"R[\x80l\r'
SECURITY_REGISTERABLE = True
SECURITY_CONFIRMABLE = False
SECURITY_CHANGEABLE = True
SECURITY_SEND_REGISTER_EMAIL = False
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = 'the salt of password hash'
SECURITY_USER_IDENTITY_ATTRIBUTES = 'name'
USER_IDENTITY_ATTRIBUTES = ['name']