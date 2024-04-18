#!/usr/bin/python3
"""
This script defines a Flask web application with one route that displays "Hello HBNB!".
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB!' when root URL is accessed."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
