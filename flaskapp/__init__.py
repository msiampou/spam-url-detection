from flask import Flask
from flaskapp.routes.routes import site

app = Flask(__name__)
app.register_blueprint(site)
