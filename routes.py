from flask import Blueprint


urls = Blueprint('urls', __name__)


@urls.route('/')
def index():
    pass

@urls.route('/animals')
def animals():
    pass

@urls.route('/animal')
def animal():
    pass

@urls.route('/animals/create')
def create_animal():
    pass