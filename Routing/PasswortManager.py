from flask import render_template, jsonify, request
from flask_security import login_required
from Application import app
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
    attributes = modelAttribute
    attributes['attributeList'] = modelAttribute.attributeList[:-1]
    pageValues = DictObj(header='Account mit Passwort', account=account, modelAttribute=attributes)
    return render_template('ShowPassword.html', pageValues=pageValues)

# ------------------------- Edit account --------------------------------------
@app.route('/editAccount/<int:id>', methods=['GET', 'POST'])
@login_required
def editAccount(id):
    form = EditForm()
    account = Account.getDictOf(id, modelAttribute.attributeList[:-1])
    if request.method == 'POST':
        account.update(form.data)
        if form.validate():
            Account.modifyDBAccount(account)
            return showPassword(id)
    else:
        form = EditForm(data=account)
    pageValues = DictObj(header='Edit Account', form=form, account=account, modelAttribute=modelAttribute)
    return render_template('EditAccount.html', pageValues=pageValues)

# ------------------------- Edit account --------------------------------------
@app.route('/generatePwd/<int:id>', methods=['GET', 'POST'])
@login_required
def generatePwd(id):
    form = GeneratePwdForm()
    account = Account.getDictOf(id, modelAttribute.attributeList[:-1])
    if request.method == 'POST':
        account.update(form.data)
        if form.validate():
            Account.modifyDBAccount(account)
            return showPassword(account['id'])
    else:
        form = GeneratePwdForm(data=account)
    attributeList = ['id', 'provider', 'username', 'question', 'answer', 'lastmodify']
    pageValues = DictObj(header='Passwort generieren', modelAttribute=modelAttribute, account=account, form=form,
                         attributeList=attributeList, ngApp='GenerateCtrl', ngCtrl='FormCtrl')
    return render_template('GeneratePwd.html', pageValues=pageValues)

@app.route('/getNewPassword', methods=['POST'])
def getNewPassword():
    definition = request.get_json()
    response = dict(error='', password='')
    print(request.values)
    try:
        length = int(definition['passwordlength'])
        generator = Generator(definition['definedcharacter'], length)
        generator.parseDefinition()
        response['password'] = generator.randomPassword()
    except ValueError:
        response['error'] = 'Die Passwortlänge muss eine Ganzzahl sein.'
    except GenerateException as error:
        print ('Fehler in: ' + error.expression)
        print(error.message)
        response['error'] = error.text

    return jsonify(response)

# ------------------------- New account --------------------------------------
@app.route('/addNewAccount', methods=['GET', 'POST'])
def addNewAccount():
    form = EditForm()
    if request.method == 'POST' and form.validate():
        id = Account.insertAccount(form.data)
        return showPassword(id)
    pageValues = DictObj(header='Neues Account Objekt erstellen', form=form, ngApp='GeneratePwd', ngCtrl='PostCtrl')
    return render_template('AddNewAccount.html', pageValues=pageValues)