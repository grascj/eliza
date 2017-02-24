from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
from response import analyze
from flask_recaptcha import ReCaptcha
#import session

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)
app.debug = True


@app.route('/')
def redir():
    return redirect(url_for('login'))


@app.route('/adduser')
def redir():
    return redirect(url_for('login'))
        if(recaptcha.verify()):



@app.route('/eliza/DOCTOR', methods=['POST'])
def doktor():
    # conversation elements
    question = request.get_json()
    resp = {'eliza': analyze(question['human'])}

    #session.storestatements(question['human'], resp['eliza'])
    # update conversation in database

    # question['human'] is the string to be responded to
    return json.dumps(resp)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        username = request.form['username']
        password = request.form['password']
    return None


if __name__ == "__main__":
    app.run(host='0.0.0.0')
