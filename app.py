from flask import Flask
from config import Config
import pymongo
import models

app = Flask(__name__)
app.config.from_object(Config)

user_name = "test value"
def db_connection():
	mongo_client = pymongo.MongoClient("mongodb+srv://mongo_base_user_1:<>@cluster0.0zbkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
	mg_db = mongo_client["maindb"]
	#breakpoint()
	return mg_db

def employees_collection():
	db = db_connection()
	#breakpoint()
	emp_collection = db["employees"]
	return emp_collection

def load_sample_data():
	emp_collection = employees_collection()
	emp_collection.remove({})
	lead_dev = { "first_name": "Lucas", "primary_address": "123 Main Street", "position": "Development Manager"}
	dev_team = [
      {"first_name": "Mia", "primary_address": "456 Harvey Milk Street", "position": "Developer"},
	  {"first_name": "Dan", "primary_address": "789 OH-strander Street", "position": "Developer"},
	  {"first_name": "Holly", "primary_address": "555 Audi Street", "position": "Developer"}
	]
	emp_collection.insert_one(lead_dev)
	emp_collection.insert_many(dev_team)
	first_record = emp_collection.find_one()
	all_records = list(emp_collection.find())
	return first_record, all_records

first_record = load_sample_data()
emp = employees_collection()
user_1 = models.Employee("bob","123 main","dev")


#breakpoint()
import routes

