from flask import render_template, jsonify, request
from flask_security import login_required
from Application import app
import datetime
from Database.Models import Account, modelAttribute
from AppForms.ExtendedForms import EditForm, GeneratePwdForm
from Utility.DictObj import DictObj
from Utility.GeneratePwd import Generator, GenerateException


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
            return showPassword(id)
    else:
        account = Account.getDictOf(id, modelAttribute.attributeList)
        form = EditForm(data=account)
    pageValues = DictObj(header='Edit Account', form=form, account=account, modelAttribute=modelAttribute)
    return render_template('EditAccount.html', pageValues=pageValues)

# ------------------------- Edit account --------------------------------------
@app.route('/generatePwd/<int:id>', methods=['GET', 'POST'])
@login_required
def generatePwd(id):
    form = GeneratePwdForm()
    if request.method == 'POST':
        if form.validate():
            account = form.data
            account['lastmodify'] = datetime.datetime.today()
            Account.modifyDBAccount(account)
            return showPassword(id)
    else:
        account = Account.getDictOf(id, modelAttribute.attributeList)
        form = GeneratePwdForm(data=account)
    attributeList = ['id', 'provider', 'username', 'question', 'answer', 'lastmodify']
    pageValues = DictObj(header='Passwort generieren', modelAttribute=modelAttribute, account=account, form=form,
                         attributeList=attributeList, ngApp='GenerateCtrl', ngCtrl='FormCtrl')
    return render_template('GeneratePwd.html', pageValues=pageValues)

@app.route('/getNewPassword', methods=['POST'])
def getNewPassword():
    definition = request.get_json()
    response = dict(error='', password='')
    print(definition)
    try:
        length = int(definition['passwordlength'])
        generator = Generator(definition['definedcharacter'], length)
        generator.parseDefinition()
        response['password'] = generator.randomPassword()
    except ValueError:
        response['error'] = 'Die Passwortlänge muss eine Ganzzahl sein.'
    except GenerateException as error:
        print ('Fehler in: ' + error.expression)
        print(error.message)                       # Return message from Exception
        response['error'] = error.text

    return jsonify(response)