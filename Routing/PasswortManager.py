from flask import render_template, jsonify, request
from Utility.DictObj import DictObj
import datetime
from flask_security import login_required

from Application import app
from Database.Models import Account, modelAttribute
from AppForms.ExtendedForms import EditForm


# ----------------------- Account list --------------------------------------
@app.route('/')
@login_required
def start():
    pageValues = DictObj(header='Liste aller Accounts', ngApp='PwdManager', ngCtrl='ListCtrl')
    return render_template('AccountList.html', pageValues=pageValues)

@app.route('/accountListData')
def loadAccountList():
    list = Account.getObjList(['id', 'provider', 'username'])
    return jsonify(list)

# ------------------------ Show password -------------------------------------
@app.route('/showPassword/<int:id>')
@login_required
def showPassword(id):
    account = Account.query.get(id).getDict(modelAttribute.attributeList)
    pageValues = DictObj(header='Account mit Passwort', account=account, modelAttribute=modelAttribute)
    return render_template('ShowPassword.html', pageValues=pageValues)

# ------------------------- Edit account --------------------------------------
@app.route('/editAccount/<int:id>', methods=['GET', 'POST'])
@login_required
def editAccount(id):
    form = EditForm()
    if request.method == 'POST':
        account = form.data
        account['lastmodify'] = datetime.datetime.today()
        if form.validate():
            Account.modifyDBAccount(account)
    else:
        account = Account.getDictOf(id, modelAttribute.attributeList)
        form = EditForm(data=account)
    pageValues = DictObj(header='Edit Account', form=form, account=account, modelAttribute=modelAttribute)
    return render_template('EditAccount.html', pageValues=pageValues)