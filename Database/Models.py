from Application import db
from flask_security import RoleMixin, UserMixin
from Utility.DictObj import DictObj
import datetime


modelAttribute = DictObj(
    id = 'Id',
    provider = 'Anbieter',
    username = 'Benutzername',
    password = 'Passwort',
    passwordlength = 'Passwortlänge',
    definedcharacter = 'Zulässige Zeichen',
    question = 'Sicherheitsfrage',
    answer = 'Antwort Sicherheitsfrage',
    lastmodify = 'Letzte Änderung',
    attributeList = ['id', 'provider', 'username', 'password', 'passwordlength', 'definedcharacter', 'question',
                     'answer', 'lastmodify']
)


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String)
    username = db.Column(db.String)
    password = db.Column(db.String)
    passwordlength = db.Column(db.Integer)
    definedcharacter = db.Column(db.String)
    question = db.Column(db.String)
    answer = db.Column(db.String)
    lastmodify = db.Column(db.DateTime)

    # Get dict from Account object.
    def getDict(self, keyList):
        origin = self.__dict__
        object = dict()
        for key in keyList:
            object[key] = origin[key]

        return object

    # Get a dict object of an account with the given id (primary key).
    @staticmethod
    def getDictOf(id, keyList):
        return Account.query.get(id).getDict(keyList)

    # Get all Account objects from database as a dictionary.
    # Dictionaries get values of keyList.
    @staticmethod
    def getObjList(keyList):
        accounts = Account.query.all()
        list = [ ]
        for account in accounts:
            object = account.getDict(keyList)
            list.append(object)

        return list

    # Modify a database entry
    @staticmethod
    def modifyDBAccount(accountDict):
        account = Account.query.get(accountDict['id'])
        account.lastmodify = datetime.datetime.today()
        a = account.__dict__
        for key in accountDict:
            if key in a and a[key] != accountDict[key]:
                account.__setattr__(key, accountDict[key])
        db.session.commit()

    @staticmethod
    def insertAccount(accountDict):
        accountDict['lastmodify'] = datetime.datetime.today()
        account = Account()
        for key in accountDict:
            account.__setattr__(key, accountDict[key])
        db.session.add(account)
        db.session.commit()

        return account.id

# ----------------------------------------------------------------------------------------
#   Flask Security
# ----------------------------------------------------------------------------------------
roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))