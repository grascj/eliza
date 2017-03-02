from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
from response import analyze
import session

application = Flask(__name__)
application.debug = True

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
    else if (request.method == 'GET'):
		key = request.args.get.('key')
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
	else:
		# check for login status
		if (session.retrievesession()):
			redirect(url_for('eliza'))
		else:	
			render_template('login.html')
		
    return None

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
