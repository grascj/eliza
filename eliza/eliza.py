from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
from response import analyze
from flask_recaptcha import ReCaptcha
import session

app = Flask(__name__)
app.debug = True

recaptcha = ReCaptcha()
recaptcha.init_app(app)
recaptcha.is_enabled = True
recaptcha.theme = "light"
recaptcha.type = "image"
recaptcha.size = "normal"
recaptcha.tabindex = 0


print(recaptcha.is_enabled)
print(recaptcha.get_code())

@app.route('/')
def redir():
    return redirect(url_for('login'))

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
		email = request.form['email']
		session.adduser(username, password, email)
		return redirect(url_for('verify'))

    return redirect(url_for('adduser'))
@app.route('/adduser', methods=['GET', 'POST'])
def addusr():
    return render_template("adduser.html")
    #if(request.method == 'POST'):
    #    if(recaptcha.verify()):
    #        return "SUCCESS"
    #    else:
    #        return "FAILURE"


@app.route('/verify', methods=['POST'])
def verifyusr():
    if(request.method == 'POST'):
        if(recaptcha.verify()):
            return "SUCCESS"
        else:
            return "FAILURE"

@app.route('/verify', methods=['GET', 'POST'])
def verify():
	if (request.method == 'POST'):
		#TODO check captcha
		key = request.form['key']
		if (session.verify(key)):
			return redirect(url_for('eliza'))
		else:
			return redirect(url_for('verify'))
	
	return redirect(url_for('verify'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']

    if (session.trylogin(username, password)):
		return redirect(url_for('eliza'))

	return None

@app.route('/logout', methods=['GET'])
def logout():
	return session.logout()

@app.route('/eliza', methods=['POST'])
def doktor():
    # conversation elements
    question = request.get_json()
    resp = {'eliza': analyze(question['human'])}

    # update conversation in database
    session.storestatements(question['human'], resp['eliza'])

    # question['human'] is the string to be responded to
    return json.dumps(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
