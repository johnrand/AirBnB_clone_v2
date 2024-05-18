#!/usr/bin/python3

"""
module of a flask web application
"""


from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """
    Returns a string hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """
    Returns string HBNB
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def dispaly_c_text(text):
    """
    Returns C followed by text variable value
    """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
