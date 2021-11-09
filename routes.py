from flask import render_template, flash, redirect
from app import app
from forms import LoginForm
from app import first_record

@app.route("/")
@app.route("/index")
def index():
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
	return render_template('index.html', title='Global Megacorp Home', posts=posts, mongo_user=first_record[0]["first_name"])
	#return render_template('temp.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route("/greeting/")
def greeting():
	return "Nice to see you"