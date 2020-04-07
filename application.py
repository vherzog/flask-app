from flask import Flask, render_template

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

if __name__ == "__main__":
    application.run()
