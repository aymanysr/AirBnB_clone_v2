#!/usr/bin/python3
"""
This script defines a Flask web application
with two routes that displays "Hello HBNB!" & "HBNB".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB!' when root URL is accessed."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display 'HBNB' when /hbnb URL is accessed."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_isfun(text):
    """Display 'C' followed by the value of the text variable
    (replace underscore _ symbols with a space  )"""
    formated_text = text.replace('_', ' ')
    return f'C {formated_text}'


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_iscool(text):
    """Display 'Python' followed by the value of the text variable
    (replace underscore _ symbols with a space  )"""
    formated_text = text.replace('_', ' ')
    return f'Python {formated_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Display 'n is a number' only if n is an integer."""
    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
