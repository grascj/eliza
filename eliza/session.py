from flask import Flask, redirect, request, url_for
from flask_mail import Mail, Message
from flaskext.mysql import MySQL
from datetime import datetime

app = Flask(__name__)

# mail setup
app.config['MAIL_SERVER']= 'smpt.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ladoftheropes@gmail.com'
app.config['MAIL_PASSWORD'] = 'depression!!!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

def storestatements(humantext, elizatext):
	return dbio.putstatement(humantext, elizatext)

def adduser(username, password, email):
	dbio.putuser(username, password, email)	
 
	# send email to user with key
    mbody = 'Your key: \n\n' + ""# some random key
    msg = Message(subject='Eliza Signup', recipients=email, body=mbody)
    mail.send(msg)
	return None

def verify(key):	
	return dbio.activateuser(key)	

def listconv():
    # return JSON array of {conv_id, start_date}
	convlist = dbio.getconvlist(session['username'])
	
	jsonlist = []
	for entry in convlist:
		jsonlist.append({'conv_id': entry['convid'], \
			'start_date': entry['startdate']})
	return jsonlist

def getconv():
    if (request.method == 'POST'):
        convid = request.form['conv_id']
        # load conversation with conv_id
        return convid

def retrievesession():
	cookie = response.cookies.get('id')
	dbio.getuser(cookie)

def trylogin(username, password):
    return dbio.checklogin(username, password)    

def logout():
    session.pop('username', None)
    session.pop('password', None)

    return redirect(url_for('eliza'))
