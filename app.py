from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run(debug=True)
