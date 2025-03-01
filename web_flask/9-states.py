#!/usr/bin/python3
'''script that starts a flask web application'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    '''remove the current SQLAlchemy Session'''
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    '''display a HTML page showing a list of states'''
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    '''display a HTML page showing a list of states'''
    states = storage.all('State').values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    else:
        return render_template('9-states.html', states=None, mode='none')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
