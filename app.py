from flask import Flask, render_template

app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'booking'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = 'list_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))


@app.route('/')
def booking():
    return render_template('booking.html')