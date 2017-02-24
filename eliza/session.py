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

# database setup
app.configapp.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)

def storestatements(humantext, elizatext):
	cursor = mysql.connect().cursor()
	cursor.execute('INSERT INTO Statement(timestamp, name, text) \
		VALUES(NOW(), ' + session['username'] + ', ' + humantext +');')
	
	cursor.execute('INSERT INTO Statement(timestamp, name, text) \
		VALUES(NOW(), Eliza, ' + elizatext + ');')



@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if (request.method == 'POST'):
	
    	# check captcha success
		if (request.form['captcha'] != 'I\'m human yo'):
	    	return redirect(url_for('/adduser'))
    
    	# add new user to database
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		cursor = mysql.connect().cursor()
		cursor.execute('INSERT INTO ElizaUser(username, password, email, status) \
			VALUES(' + username + ', ' + password + ', ' + email + ', disabled);')
		# send email to user with key
		mbody = 'Your key: \n\n' + #some random key
		msg = Message(subject='Eliza Signup', recipients=email, body=mbody)
		mail.send(msg)
		return redirect(url_for('/adduser'))

@app.route('/verify', methods=['GET', 'POST'])
def verify():
	if (request.method == 'POST'):
		

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
