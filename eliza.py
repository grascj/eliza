from flask import Flask, render_template
import datetime

application = Flask(__name__)
application.debug = True

@application.route("/")
def hello():
	return render_template("index.html");


@application.route("/eliza/",methods=["GET","POST"])
def outhere():
	name=request.form['name']
	cur=datetime.datetime.now()
	date=cur.strftime("%Y-%m-%d %H:%M")
	return date;
		

@application.route("/eliza/DOCTOR/")
def doktor():
	return "<h1 style='color:red'>DOKTOR</h1>"

if __name__ == "__main__":
	application.run(host='0.0.0.0')
