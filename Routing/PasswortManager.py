from flask import render_template, jsonify

from Application import app
from Database.Models import Account


@app.route('/')
def start():
    pageValues = dict(header='Liste aller Accounts', ngApp='PwdManager', ngCtrl='ListCtrl')
    return render_template('AccountList.html', pageValues=pageValues)

@app.route('/accountListData')
def loadAccountList():
    list = Account.getObjList(['id', 'provider', 'username'])
    return jsonify(list)