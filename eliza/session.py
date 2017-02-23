from flask import Flask, redirect, request, url_for
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

app.config['MAIL_SERVER']= 'smpt.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'ladoftheropes@gmail.com'
app.config['MAIL_PASSWORD'] = 'depression!!!'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

userDict = {['username']:, 'password':}
convlistDict = {['username']:, 'convist':}
convDict = {['id']:, 'start_date':, 'conv':}
statement = {['timestamp']:, 'name':, 'text'}

def storestatement(timestamp, name, text):
	# add statement entry
	statement['timestamp'] = timestamp
    statement['name'] = name
	statement['text'] = text

	# add statement to convDict
	convDict['id'] = len(convDict)
    convDict['start_date'] = datetime.now().time()
    convDict['text'] = text

    # add convDict to convlistDict
	convlistDict

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if (request.method == 'POST'):
	
        # check captcha success
	if (request.form['captcha'] != 'I\'m human yo'
	    return redirect(url_for('/adduser'))
    
        # Send email to user with key
	email = response.form['email']
	mbody = 'Your key: \n\n' + #some random key
	msg = Message(subject='Eliza Signup', recipients=email, body=mbody)
	mail.send(msg)
	return redirect(url_for('/adduser'))

@app.route('/verify', methods=['GET', 'POST'])
def verify():


@app.route('/listconv')
def listconv():
    # return JSON array of {conv_id, start_date}

@app.route('/getconv', methods=['GET', 'POST'])
def getconv():
    if (request.method == 'POST'):
	convid = request.form['conv_id']
	# load conversation with conv_id

@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
	username = request.form['username']
	password = request.form['password']
	
	resp.set_cookie('info', username + ',' + password)
	
	return resp

    if #already logged in before
	info = request.cookies.get('info')
	info = info.split(',')
        username = info[0]
	password = info[1]

	return redirect(url_for('eliza')) 

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)

    return redirect(url_for('eliza'))
