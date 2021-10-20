from flask import flask

app = flask(__name__)

@app.route("/")
def index():
	return "Hello Wolford"

@app.route("/greeting/")
def greeting():
	return "Nice to see you"