from codecs import escape_decode
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://abdou:passer@localhost:5432/udabase_modeling'

db = SQLAlchemy(app)

class Animal(db.Model):
    __tablename__ = 'animals'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100))
    espece = db.Column(db.String(20))
    age = db.Column(db.Integer)
    couleur = db.Column(db.String(15))

class Child(db.Model):
    pass

db.create_all()

@app.route('/')
def index():
    return 'Hello World!'
    
