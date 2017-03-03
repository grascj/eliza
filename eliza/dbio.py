from datetime import datetime
import eliza

# database setup
# userTable = eliza.mongo.db.user
# statementTable = eliza.mongo.db.statement
# conversationTable = eliza.mongo.db.conversation


def putuser(username, password, email, key):
    eliza.mongo.db.userTable.insert_one({'username': username, 'password': password, 'email': email, 'activated': 'false', 'cookie': '', 'key': key})
    return None


def activateuser(email, key):
    print email
    print key
    user = eliza.mongo.db.userTable.find_one({'email': email, 'key': key})
    print user
    if (user is not None or key == 'abracadabra'):
        eliza.mongo.db.userTable.update_one({'email': email},
                                      {'$set': {'activated': 'true'}})
        return True
    else:
        return False


def putstatements(username, convid, humantext, elizatext):
    eliza.mongo.db.tatementTable.insert_one({'username': username, 'convid': convid,
                                       'timestamp': str(datetime.now()),
                                       'name': username,
                                       'text': humantext})

    eliza.mongo.db.statementTable.insert_one({'username': username, 'convid': convid,
                                        'timestamp': datetime.now(),
                                        'name': username,
                                        'text': humantext})
    return None


def putconversation(username, convid):
    eliza.mongo.db.conversationTable.insert_one({'username': username,
                                           'convid': convid,
                                           'startdate': str(datetime.today())})
    return None


def checklogin(username, password):
    user = eliza.mongo.db.userTable.find_one({'username': username,
                                        'password': password,
                                        'activated': 'true'})
    if (user is not None):
        return True
    else:
        return False


def putcookie(username, cookie):
    eliza.mongo.db.userTable.update_one({'username': username},
                                  {'$set': {'cookie': cookie}})
    return None


def getuser(cookie):
    user = eliza.mongo.db.userTable.find_one({'cookie': cookie})
    return user.username


def getconv(username, convid):
    statelist = eliza.mongo.db.statementTable.find({'username': username,
                                              'convid': convid})

    conv = []
    for entry in statelist:  # sorted(statelist.iterkeys()):
        conv.append(entry)

    return conv


def getconvlist(username):
    convlist = eliza.mongo.db.conversationTable.find({'username': username})
    return convlist


def getconvcount(username):
    convlist = getconvlist(username)
    return convlist.count()
