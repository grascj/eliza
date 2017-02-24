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

def putstatements(humantext, elizatext):
	cursor.execute('INSERT INTO Statement(name, text) \
		VALUES(' + session['username'] + ', ' + humantext + ');')
	
	cursor.execute('INSERT INTO Statement(name, text) \
		VALUES( Eliza, ' + elizatext + ');')

def putconversation(username)
	cursor.execute('COUNT * FROM Conversation WHERE username = ' + username')')
	convid = cursor.getone()

	cursor.execute('INSERT INTO Conversation(username, convid) \
		VALUES(' + username + ', ' + convid + ');')

def checklogin(username, password):
	cursor.execute('SELECT * FROM ElizaUser WHERE username = ' + username + ' AND  \
		password = ' + password + ' AND activated = true')

	user = cursor.getone()
	if (user == None):
		return false
	
	return true

def getconv(username, convid):
	cursor.execute('SELECT * FROM Conversation WHERE username = ' + username \
		+ 'AND convid = ' + convid + ' ORDER BY timestamp DESC')
	
	conv = []
	while ((entry = cursor.getone()) != None):
		conv.append(entry)

	return conv

def getconvlist(username):
	cursor.execute('SELECT * FROM Conversation WHERE username = ' + username)

	convlist = []
	while ((conv = cursor.getone()) != None):
		convlist.append(conv)

	return convlist



