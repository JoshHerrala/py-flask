from flask import render_template, flash, redirect, request
from app import app
from forms import LoginForm
from app import first_record, emp

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

@app.route('/employees', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		return render_template('create_employee.html')
 
	if request.method == 'POST':
		#breakpoint()
		#employee_id = request.form['employee_id']
		first_name = request.form['first_name']
		primary_address = request.form['primary_address']
		#position = request.form['position']
		# employee = EmployeeModel(employee_id=employee_id, name=name, age=age, position = position)
		# db.session.add(employee)
		# db.session.commit()
		new_employee = { "first_name": first_record, "primary_address": primary_address}
		#breakpoint()
		#TODO import collection from app
		emp.insert_one(new_employee)
		return redirect('/index')