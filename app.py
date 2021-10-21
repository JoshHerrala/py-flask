from flask import Flask
from flask import render_template

#TODO, refactor to seperate routing file
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	user = {'username': 'Lucas'}
	return render_template('index.html', title='Global Megacorp Home', user=user)

@app.route("/greeting/")
def greeting():
	return "Nice to see you"