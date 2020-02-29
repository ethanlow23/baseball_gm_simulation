from flask import Flask
from api.home_api import home_api

app = Flask(__name__)

app.register_blueprint(home_api)
