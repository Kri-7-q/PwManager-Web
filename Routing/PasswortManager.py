from flask import render_template, jsonify
from Utility.DictObj import DictObj

from Application import app
from Database.Models import Account, attributeList
from AppForms.ExtendedForms import EditForm

# ----------------------- Account list --------------------------------------
@app.route('/')
def start():
    pageValues = dict(header='Liste aller Accounts', ngApp='PwdManager', ngCtrl='ListCtrl')
    return render_template('AccountList.html', pageValues=pageValues)

@app.route('/accountListData')
def loadAccountList():
    list = Account.getObjList(['id', 'provider', 'username'])
    return jsonify(list)

# ------------------------ Show password -------------------------------------
@app.route('/showPassword/<int:id>')
def showPassword(id):
    account = Account.query.get(id).getDict(attributeList)
    pageValues = dict(header='Account mit Passwort', account=account, accountAttributes=attributeList)
    return render_template('ShowPassword.html', pageValues=pageValues)

# ------------------------- Edit account --------------------------------------
@app.route('/editAccount/<int:id>')
def editAccount(id):
    account = Account.getDictOf(id, attributeList)
    form = EditForm(data=account)
    pageValues = DictObj(header='Edit Account', form=form)
    return render_template('EditAccount.html', pageValues=pageValues)