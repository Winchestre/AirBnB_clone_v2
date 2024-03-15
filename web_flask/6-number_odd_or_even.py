#!/usr/bin/python3
"""start a simple Flask web application"""
from flask import Flask
from flask import render_template
from markupsafe import escape

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def Hello_HBNB():
    """Display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def Hbnb():
    """Display HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Display variable"""
    return f"C {escape(text).replace('_', ' ')}"


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    """Display variable"""
    return f"Python {escape(text).replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    """Display HBNB"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>')
def number_template(n):
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
