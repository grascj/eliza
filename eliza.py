from flask import Flask, jsonify, render_template, request
import datetime
import re
import random
 

application = Flask(__name__)
application.debug = True


@application.route("/")
def hello():
    return render_template("index.html")


@application.route("/eliza/", methods=["GET", "POST"])
def outhere():
    if(request.method == "POST"):
        name = request.form["name"]
        cur = datetime.datetime.now()
        date = cur.strftime("%Y-%m-%d %H:%M:%S")
        return render_template("eliza.html", name=name, date=date)
    else:
        return render_template("eliza.html")


@application.route("/eliza/DOCTOR", methods=["POST"])
def doktor():
    question = request.get_json()
    # test comment
    return analyze(question)["eliza"]
 
if __name__ == "__main__":
    application.run(host='0.0.0.0')
