from flask import redirect, request, session, url_for
from flask_mail import Mail, Message
import dbio
import random
import string
import eliza

# mail setup
eliza.application.config['MAIL_SERVER'] = 'smpt.gmail.com'
eliza.application.config['MAIL_PORT'] = 465
eliza.application.config['MAIL_USERNAME'] = 'ladoftheropes@gmail.com'
eliza.application.config['MAIL_PASSWORD'] = 'depression!!!'
eliza.application.config['MAIL_USE_TLS'] = False
eliza.application.config['MAIL_USE_SSL'] = True
mail = Mail(eliza.application)


def storestatements(humantext, elizatext):
    return dbio.putstatement(session['username'], humantext, elizatext)


def adduser(username, password, email):
    dbio.putuser(username, password, email)

    # send email to user with key
    mbody = 'Your key: \n\n' + ""  # some random key
    msg = Message(subject='Eliza Signup', recipients=email, body=mbody)
    mail.send(msg)
    return None


def generatekey():
    return ''.join(random.choice(string.ascii_letters + string.digits)
                   for x in range(15))


def verify(key):
    return dbio.activateuser(key)


def listconv():
    # return JSON array of {conv_id, start_date}
    convlist = dbio.getconvlist(session['username'])

    jsonlist = []
    for entry in convlist:
        jsonlist.append({'conv_id': entry['convid'],
                         'start_date': entry['startdate']})
    return jsonlist


def getconv():
    if (request.method == 'POST'):
        convid = request.form['conv_id']
        # load conversation with conv_id
        return convid


def retrievesession():
    cookie = request.cookies.get('id')
    if (cookie is None):
        return False

    session['username'] = dbio.getuser(cookie)
    return True


def trylogin(username, password):
    if (dbio.checklogin(username, password)):
        session['username'] = username
        return True
    else:
        return False


def logout():
    session.pop('username', None)

    return redirect(url_for('login'))
