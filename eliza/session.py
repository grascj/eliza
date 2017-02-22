from flask import Flask, redirect, request, url_for
app = Flask(__name__)

@app.route('/adduser', methods=['GET', 'POST'])
def adduser():
    

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
