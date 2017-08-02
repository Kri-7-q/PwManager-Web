from Application import db


attributeList = ['id', 'provider', 'username', 'password', 'passwordlength', 'definedcharacter', 'question',
                     'answer', 'lastmodify']

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
        account.provider = accountDict['provider']
        account.username = accountDict['username']
        account.password = accountDict['password']
        account.passwordlength = accountDict['passwordlength']
        account.question = accountDict['question']
        account.answer = accountDict['answer']
        account.definedcharacter = accountDict['definedcharacter']
        account.lastmodify = accountDict['lastmodify']
        db.session.commit()