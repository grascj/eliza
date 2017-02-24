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

def putstatements(humantext, elizatext):
	cursor.execute('INSERT INTO Statement(timestamp, name, text) \
		VALUES(NOW(), ' + session['username'] + ', ' + humantext + ');')
	
	cursor.execute('INSERT INTO Statement(timestamp, name, text) \
		VALUES(NOW(),  Eliza, ' + elizatext + ');')

def getconv(convid):
	cursor.execute('SELECT * FROM Conversation WHERE convid = ' + convid + \
		' ORDER BY(timestamp));')
	
	conv = []
	while ((entry = cursor.getone()) != None):
		contList.append(entry)

	return conv

def getconvlist():
	cursor.execute('SELECT * FROM'

def put
