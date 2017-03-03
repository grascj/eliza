from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail
from flask_pymongo import PyMongo
import json
from response import analyze
import session

application = Flask(__name__)
#  MongoDB Config
application.debug = True
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


@application.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        session.adduser(username, password, email)
        return redirect(url_for('verify'))
    else:
        return render_template('adduser.html')


@application.route('/verify', methods=['GET', 'POST'])
def verify():
    if (request.method == 'POST'):
        key = request.form['key']
    elif (request.method == 'GET'):
        key = request.args.get('key')
    else:
        return render_template('verify.html')

    if (session.verify(key)):
        return redirect(url_for('eliza'))
    else:
        return render_template('verify.html', msg='Incorrect key')


@application.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
        if (session.trylogin(username, password)):
            return redirect(url_for('eliza'))
    elif (session.retrievesession()):
        return redirect(url_for('eliza'))
    else:
        return render_template('login.html')


@application.route('/logout', methods=['GET'])
def logout():
    return session.logout()


@application.route('/eliza', methods=['POST'])
def doktor():
    # conversation elements
    question = request.get_json()
    resp = {'eliza': analyze(question['human'])}

    # update conversation in database
    session.storestatements(question['human'], resp['eliza'])

    # question['human'] is the string to be responded to
    return json.dumps(resp)

if __name__ == "__main__":
    application.run(host='0.0.0.0')
