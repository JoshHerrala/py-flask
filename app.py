from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
user_name = "test value"
import routes