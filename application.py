from flask import Flask, render_template, session

app.secret_key = 'chesneyandozy'
app.config['SESSION_TYPE'] = 'filesystem'

application = Flask(__name__)
application.debug = True

@application.route('/', methods=['GET'])
def home():
    return render_template("home.html")

@application.route('/about', methods=['GET'])
def about():
    return render_template("about.html")

@application.route('/welcome/<name>', methods=['GET'])
def welcome(name):
    return '<h1>Hello there, ' + name + '!</h1>'

@application.rote('/session')
def session():
    count = session.get('count', None)
    if not count:
        session['count'] = 1
    elif count >= 10:
        session.clear()
        return "The session has been cleared"
    else:
        session['count'] += 1
        return "The total number of refreshes for this user is: " + string(sesssion['count'])

if __name__ == "__main__":
    application.run()
