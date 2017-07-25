from Application import db

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