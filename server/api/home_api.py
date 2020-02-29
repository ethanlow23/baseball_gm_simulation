from flask import Blueprint, jsonify

home_api = Blueprint('home_api', __name__)

@home_api.route('/')
def home():
    return jsonify({"msg": "hellooo world"})
