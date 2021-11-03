from flask import Flask
from config import Config
import pymongo


app = Flask(__name__)
app.config.from_object(Config)
user_name = "test value"
client = pymongo.MongoClient("mongodb+srv://mongo_base_user_1:<PZZWERD>@cluster0.0zbkf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
#breakpoint()
import routes