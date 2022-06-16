from flask import Blueprint

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Upload CSV</h1>"

@views.route('/select')
def select():
    return "<h1>Selecting students</h1>"
