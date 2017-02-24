from flask import Flask
from flaskext.mysql import MySQL

# database setup
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'password'
app.config['MYSQL_DATABASE_DB'] = 'ElizaDB'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(app)
cursor = mysql.connect().cursor() 

def putuser(username, password, email):
	cursor.execute('INSERT INTO ElizaUser(username, password, email) \
		VALUES(' + username + ', ' + password + ', ' + email + ');')

def activateuser(username, key):
	cursor.execute('SELECT * ElizaUser WHERE username = ' + username +\
		' AND key = ' + key)
	user = cursor.fetchone()

	if (user == None):
		return False
	
	

def putstatements(humantext, elizatext):
	cursor.execute('INSERT INTO Statement(name, text) \
		VALUES(' + session['username'] + ', ' + humantext + ');')
	
	cursor.execute('INSERT INTO Statement(name, text) \
		VALUES( Eliza, ' + elizatext + ');')

def putconversation(username)
	cursor.execute('COUNT * FROM Conversation WHERE username = ' + username')')
	convid = cursor.fetchone()

	cursor.execute('INSERT INTO Conversation(username, convid) \
		VALUES(' + username + ', ' + convid + ');')

def checklogin(username, password):
	cursor.execute('SELECT * FROM ElizaUser WHERE username = ' + username + ' AND  \
		password = ' + password + ' AND activated = true')

	user = cursor.fetchone()
	if (user == None):
		return False
	
	# login SUCCESS, add cookie to ElizaUser instance
	cursor.execute('UPDATE ElizaUser cookie = ' + cookie + ' WHERE username = ' + \
		username)
	return True

def getuser(cookie):
	cursor.execute('SELECT * FROM ElizaUser WHERE cookie = ' + cookie)
	
	user = cursor.fetchone()
	return user.username

def getconv(username, convid):
	cursor.execute('SELECT * FROM Conversation WHERE username = ' + username \
		+ 'AND convid = ' + convid + ' ORDER BY timestamp DESC')
	
	conv = []
	while ((entry = cursor.fetchone()) != None):
		conv.append(entry)

	return conv

def getconvlist(username):
	cursor.execute('SELECT * FROM Conversation WHERE username = ' + username)

	convlist = []
	while ((conv = cursor.fetchone()) != None):
		convlist.append(conv)

	return convlist



