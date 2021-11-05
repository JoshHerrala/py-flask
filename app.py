from flask import Flask
from config import Config
import pymongo

app = Flask(__name__)
app.config.from_object(Config)

user_name = "test value"
def db_connection():
	mongo_client = pymongo.MongoClient("mongodb+srv://mongo_base_user_1:<pzz>@cluster0.0zbkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
	mg_db = mongo_client["maindb"]
	return mg_db

def load_sample_data():
	client = db_connection()
	#breakpoint()
	emp_collection = client["employees"]
	client.employees.remove({})
	emp1 = { "first_name": "Lucas", "primary_address": "123 Main Street"}
	emp_collection.insert_one(emp1)
	first_record = emp_collection.find_one()
	#breakpoint()
	return first_record

first_record = load_sample_data()
import routes

#breakpoint()
#find all
#array = list(emp_collection.find())
#client.list_collection_names()
