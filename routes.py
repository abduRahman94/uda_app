from flask import Blueprint, render_template


urls = Blueprint('urls', __name__)


@urls.route('/')
def index():
    return render_template('index.html')

@urls.route('/animals')
def animals():
    pass

@urls.route('/animal')
def animal():
    pass

@urls.route('/animals/create')
def create_animal():
    pass