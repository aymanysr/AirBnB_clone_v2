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
    return 'C' + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
