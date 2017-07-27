from flask import render_template, jsonify

from Application import app
from Database.Models import Account


@app.route('/')
def start():
    pageValues = dict(header='Liste aller Accounts', ngApp='AccountList', ngCtrl='ListController')
    return render_template('AccountList.html', pageValues=pageValues)

@app.route('/accountListData')
def accountListData():
    list = Account.getObjList(['id', 'provider', 'username'])
    return jsonify(list)