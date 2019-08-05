from flask import Blueprint, jsonify

api = Blueprint(import_name=__name__, name='api', url_prefix='/api/')


@api.route('')
def index():
    return jsonify({'message': 'Welcome to flask_minimal_app API!', 'result': True})
