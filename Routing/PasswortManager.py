from flask import render_template, jsonify, request
from Utility.DictObj import DictObj
import datetime

from Application import app
from Database.Models import Account, attributeList
from AppForms.ExtendedForms import EditForm

# ----------------------- Account list --------------------------------------
@app.route('/')
def start():
    pageValues = DictObj(header='Liste aller Accounts', ngApp='PwdManager', ngCtrl='ListCtrl')
    return render_template('AccountList.html', pageValues=pageValues)

@app.route('/accountListData')
def loadAccountList():
    list = Account.getObjList(['id', 'provider', 'username'])
    return jsonify(list)

# ------------------------ Show password -------------------------------------
@app.route('/showPassword/<int:id>')
def showPassword(id):
    account = Account.query.get(id).getDict(attributeList)
    pageValues = DictObj(header='Account mit Passwort', account=account, accountAttributes=attributeList)
    return render_template('ShowPassword.html', pageValues=pageValues)

# ------------------------- Edit account --------------------------------------
@app.route('/editAccount/<int:id>', methods=['GET', 'POST'])
def editAccount(id):
    form = EditForm()
    if request.method == 'POST':
        account = form.data
        account['lastmodify'] = datetime.datetime.today()
        if form.validate():
            Account.modifyDBAccount(account)
    else:
        account = Account.getDictOf(id, attributeList)
        form = EditForm(data=account)
    pageValues = DictObj(header='Edit Account', form=form, account=account)
    return render_template('EditAccount.html', pageValues=pageValues)