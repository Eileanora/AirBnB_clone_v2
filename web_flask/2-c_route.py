#!/usr/bin/python3
'''script that starts a flask web application'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''hello function'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''hbnb function'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''c function'''
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
