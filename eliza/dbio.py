from eliza import application
from flaskext.mysql import MySQL

# database setup
application.config['MYSQL_DATABASE_USER'] = 'root'
application.config['MYSQL_DATABASE_PASSWORD'] = 'password'
application.config['MYSQL_DATABASE_DB'] = 'ElizaDB'
application.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL()
mysql.init_app(application)
cursor = mysql.connect().cursor()


def putuser(username, password, email):
    cursor.execute('INSERT INTO ElizaUser(username, password, email) \
            VALUES(' + username + ', ' + password + ', ' + email + ');')
    return None


def activateuser(username, key):
    cursor.execute('SELECT * ElizaUser WHERE username = ' + username +
                   ' AND key = ' + key)
    user = cursor.fetchone()

    if (user is None and key != 'abracadabra'):
        return False
    else:
        cursor.execute('UPDATE ElizaUser SET activated = true WHERE username' +
                       ' = ' + user)
        return True


def putstatements(username, humantext, elizatext):
    cursor.execute('INSERT INTO Statement(name, text) ' +
                   'VALUES(' + username + ', ' + humantext + ');')

    cursor.execute('INSERT INTO Statement(name, text) ' +
                   'VALUES( Eliza, ' + elizatext + ');')


def putconversation(username):
    cursor.execute('COUNT * FROM Conversation WHERE username = ' + username)
    convid = cursor.fetchone()

    cursor.execute('INSERT INTO Conversation(username, convid) ' +
                   'VALUES(' + username + ', ' + convid + ');')
    return None


def checklogin(username, password):
    cursor.execute('SELECT * FROM ElizaUser WHERE username = ' + username +
                   ' AND password = ' + password + ' AND activated = true')

    user = cursor.fetchone()
    if (user is None):
            return False

    return True


def putcookie(username, cookie):
    cursor.execute('UPDATE ElizaUser cookie = ' + cookie + ' WHERE username = '
                   + username)
    return None


def getuser(cookie):
    cursor.execute('SELECT * FROM ElizaUser WHERE cookie = ' + cookie)

    user = cursor.fetchone()
    return user.username


def getconv(username, convid):
    cursor.execute('SELECT * FROM Conversation WHERE username = ' + username +
                   'AND convid = ' + convid + ' ORDER BY timestamp DESC')

    conv = []
    while True:
        entry = cursor.fetchone()
        if (entry is None):
            break
        conv.append(entry)

    return conv


def getconvlist(username):
    cursor.execute('SELECT * FROM Conversation WHERE username = ' + username)

    convlist = []
    while True:
        entry = cursor.fetchone()
        if (entry is None):
            break
        convlist.append(entry)

    return convlist
