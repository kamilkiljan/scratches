from flask import Flask

from main.views import main
from api.views import api

app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(api)