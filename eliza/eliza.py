from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_mail import Mail
from flask_pymongo import PyMongo
import json
from response import analyze
import session
import datetime

application = Flask(__name__)
application.secret_key = "super secret key"
#  MongoDB Config
# application.debug = True
application.config['MONGO_DBNAME'] = 'elizaDB'
mongo = PyMongo(application, config_prefix='MONGO')
#  Flask-Mail Config
application.config['MAIL_SERVER'] = 'smtp.gmail.com'
application.config['MAIL_PORT'] = 465
application.config['MAIL_USERNAME'] = 'shanekennedy7134'
application.config['MAIL_PASSWORD'] = 'groggy7134'
application.config['MAIL_USE_TLS'] = False
application.config['MAIL_USE_SSL'] = True
mail = Mail(application)


@application.route('/')
def redir():
    return redirect(url_for('login'))


@application.route('/adduser/', methods=['GET', 'POST'])
def adduser():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        session.adduser(username, password, email)
        return redirect(url_for('verify'))
    else:
        return render_template('adduser.html')


@application.route('/verify/', methods=['GET', 'POST'])
def verify():
    if (request.method == 'POST'):
        key = request.form['key']
        email = request.form['email']
    elif (request.method == 'GET'):
        if('key' in request.args.keys()):
            key = request.args.get('key')
            email = request.args.get('email')
        else:
            return render_template('verify.html')

    f (session.verify(email, key)):
        return redirect(url_for('eliza_p'))
    else:
        return render_template('verify.html', msg='Incorrect key')


@application.route('/login/', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        if (session.trylogin(username, password)):
            return redirect(url_for('eliza_p'))
        else:
            return render_template('login.html')
    elif (session.retrievesession()):
        return redirect(url_for('eliza_p'))
    else:
        return render_template('login.html')


@application.route('/logout/', methods=['GET'])
def logout():
    return session.logout()


@application.route('/listconv/', methods=['GET', 'POST'])
def listconv():
    #  List all past conversations from current user
    convlist = session.listconv()
    return jsonify(convlist)


@application.route('/getconv/', methods=['GET', 'POST'])
def getconv():
    #  Returns {status:'OK', conversation:[{timestamp:, name:, text:},...]}
    convid = request.form['convid']
    conv = session.getconv(convid)
    return json.dumps(conv)


@application.route('/eliza/', methods=['GET', 'POST'])
def eliza_p():
    cur = datetime.datetime.now()
    date = str(cur.strftime('%Y-%m-%d %H:%M:%S'))
    name = session.session['username']
    return render_template('eliza.html', name=name, date=date)


@application.route('/eliza/DOCTOR', methods=['POST'])
def doctor():
    question = request.get_json()
    resp = {'eliza': analyze(question['human'])}
    session.storestatements(question, resp['eliza'])
    return json.dumps(resp)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
