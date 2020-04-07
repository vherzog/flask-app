from flask import Flask, render_template, session

application = Flask(__name__)
application.debug = True
application.secret_key = 'chesneyandozy'
application.config['SESSION_TYPE'] = 'filesystem'

@application.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@application.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@application.route('/welcome/<name>', methods=['GET'])
def welcome(name):
    return '<h1>Hello there, ' + name + '!</h1>'

@application.route('/session')
def sessions():
    count = session.get('count', None)
    if not count:
        session['count'] = 1
    elif count >= 10:
        session.clear()
        session['count'] = 1
        return "The session has been cleared"
    else:
        session['count'] += 1
        return "The total number of refreshes for this user is: " + str(session['count'])
    return "Count has begun..."

@application.route('/<int:page>')
def pageNum(page):
    p = session.get('sum', None)
    if not p:
        session['sum'] = page
    elif p > 100:
        session.clear()
        return "Oops! You went over 100. Your session has been cleared."
    else:
        session['sum'] += page
    return "<p>Congrats! You successfully opened this page. Add /{NUMBER} to continuing counting.\n Current count: " + str(session['sum']) + ".</p>"


if __name__ == "__main__":
    application.run()
