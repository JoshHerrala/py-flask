from flask import render_template
from app import app
from app import user_name


@app.route("/")
@app.route("/index")
def index():
	user = {'username': user_name }
	posts = [
        {
            'author': {'username': 'Mia'},
            'body': 'Beautiful day in San Franciso!'
        },
        {
            'author': {'username': 'Rob'},
            'body': 'The Pittsburgh SV-1 is daft!'
        }
    ]
	return render_template('index.html', title='Global Megacorp Home', user=user, posts=posts)

@app.route("/greeting/")
def greeting():
	return "Nice to see you"