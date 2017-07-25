from flask import render_template, jsonify

from Application import app
from Database.Models import Account


@app.route('/')
def start():
    pageValues = dict(header='Liste aller Accounts')
    return render_template('AccountList.html', pageValues=pageValues)

@app.route('/accountList')
def getAccountList():
    list = Account.getObjList(['id', 'provider', 'username', 'password'])
    return jsonify(list)