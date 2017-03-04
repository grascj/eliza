from flask import redirect, request, session, url_for
from flask_mail import Message
import dbio
import random
import string
import eliza


def storestatements(humantext, elizatext):
    return dbio.putstatements(session['username'], session['convid'],
                              humantext, elizatext)


def adduser(username, password, email):
    key = generatekey()
    dbio.putuser(username, password, email, key)

    # send email to user with key
    mbody = 'Your key: \n\n' + key  # some random key
    msg = Message(subject='Eliza Signup', sender='ladoftheropes@gmail.com', recipients=[email], body=mbody)
    eliza.mail.send(msg)
    return None


def generatekey():
    return ''.join(random.choice(string.ascii_letters + string.digits)
                   for x in range(15))


def verify(email, key):
    return dbio.activateuser(email, key)


def listconv():
    # return JSON array of {conv_id, start_date}
    convlist = dbio.getconvlist(session['username'])
    jsonlist = []
    for entry in convlist:
        jsonlist.append({'convid': entry['convid'],
                         'startdate': entry['startdate']})
    return jsonlist


def getconv(username, convid):
    # load conversation with convid
    return dbio.getconv(username, convid)


def retrievesession():
    cookie = request.cookies.get('id')
    if (cookie is None):
        return False

    session['username'] = dbio.getuser(cookie)
    session['convid'] = dbio.getconvcount(session['username'])
    return True


def trylogin(username, password):
    if (dbio.checklogin(username, password)):
        session['username'] = username
        session['convid'] = dbio.getconvcount(username)
        return True
    else:
        return False


def logout():
    dbio.putconversation(session['username'], session['convid'])
    session.pop('username', None)
    session.pop('convid', None)
    return redirect(url_for('login'))


def getsession():
    sess = {'username': session['username'], 'convid': session['convid']}
