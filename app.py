from flask import Flask
from config import Config
import pymongo


app = Flask(__name__)
app.config.from_object(Config)
user_name = "test value"
mongo_client = pymongo.MongoClient("mongodb+srv://mongo_base_user_1:<pazzwerd>@cluster0.0zbkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")

mg_db = mongo_client["maindb"]

emp_collection = mg_db["employees"]

emp1 = { "first_name": "Lucas", "primary_address": "123 Main Street"}
#breakpoint()
x = emp_collection.insert_one(emp1)
bork = emp_collection.find_one()

#breakpoint()
import routes