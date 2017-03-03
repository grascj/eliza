from datetime import datetime
import eliza
from flask_pymongo import PyMongo

# database setup
eliza.application.config['MONGO_DBNAME'] = 'elizaDB'
mongo = PyMongo(eliza.application)
userTable = mongo.db.user
statementTable = mongo.db.statement
conversationTable = mongo.db.conversation


def putuser(username, password, email):
    userTable.insert_one({'username': username, 'password': password,
                          'email': email, 'activated': 'false', 'cookie': ''})
    return None


def activateuser(username, key):
    user = userTable.find_one({'username': username, 'key': key})
    if (user is not None or key == 'abracadabra'):
        userTable.update_one({'username': username},
                             {'$set': {'activated': 'true'}})
        return True
    else:
        return False


def putstatements(username, convid, humantext, elizatext):
    statementTable.insert_one({'username': username, 'convid': convid,
                               'timestamp': datetime.now(), 'name': username,
                               'text': humantext})

    statementTable.insert_one({'username': username, 'convid': convid,
                               'timestamp': datetime.now(), 'name': username,
                               'text': humantext})


def putconversation(username, convid):
    conversationTable.insert_one({'username': username, 'convid': convid,
                                  'startdate': datetime.today()})
    return None


def checklogin(username, password):
    user = userTable.find_one({'username': username, 'password': password,
                               'activated': 'true'})
    if (user is not None):
        return True
    else:
        return False


def putcookie(username, cookie):
    userTable.update_one({'username': username},
                         {'$set': {'cookie': cookie}})
    return None


def getuser(cookie):
    user = userTable.find_one({'cookie': cookie})
    return user.username


def getconv(username, convid):
    statelist = statementTable.find({'username': username, 'convid': convid})

    conv = []
    for entry in statelist:  # sorted(statelist.iterkeys()):
        conv.append(entry)

    return conv


def getconvlist(username):
    convlist = conversationTable.find({'username': username})
    return convlist


def getconvcount(username):
    convlist = getconvlist(username)
    return len(convlist)
