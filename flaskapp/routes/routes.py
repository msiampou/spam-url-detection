from flask import render_template
from flask import request
from flask import Blueprint
from train import predict as make_prediction

site = Blueprint('site', __name__, template_folder='templates')


@site.route("/")
def home():
    return render_template('home.html')


@site.route("/predict", methods=['POST'])
def predict():
    given_url = request.form['url']
    prediction = make_prediction(given_url)
    if prediction == 0:
        return render_template('benign.html', url=given_url)
    else:
        return render_template('malicious.html', url=given_url)
