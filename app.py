from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
	return "Hello Wolford"

@app.route("/greeting/")
def greeting():
	return "Nice to see you"