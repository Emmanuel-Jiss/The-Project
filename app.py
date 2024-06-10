from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='website/templates', static_folder='website/static')


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/booking')
def booking():
    return render_template('booking.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/account')
def account():
    return render_template('account.html')


if __name__ == '__main__':
    app.run(debug=True)

USERNAME = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'booking'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + USERNAME + ':' + PASSWORD + '@' + HOST + '/' + DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Item(db.Model):
    __tablename__ = 'boooking'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
