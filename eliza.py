from flask import Flask, render_template, request
import datetime

application = Flask(__name__)
application.debug = True

@application.route("/")
def hello():
    return render_template("index.html");


@application.route("/eliza/",methods=["GET","POST"])
def outhere():
    if(request.method == "POST"):
        print('POST')
        name=request.form["name"]
        cur=datetime.datetime.now()
        date=cur.strftime("%Y-%m-%d %H:%M")
        return render_template("eliza.html",name=name,date=date);
    else:
        print('NOT POST')
        return render_template("eliza.html")


@application.route("/eliza/DOCTOR/",methods=["POST"])
def doktor():
    question = request.get_json()
    #test comment
    return question["human"]




#for getting eliza's response
def therapy(sentence):
    return sentence



if __name__ == "__main__":
    application.run(host='0.0.0.0')

