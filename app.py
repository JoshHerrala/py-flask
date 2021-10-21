from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	user = {'username': 'Lucas'}
	return render_template('index.html')

@app.route("/greeting/")
def greeting():
	return "Nice to see you"