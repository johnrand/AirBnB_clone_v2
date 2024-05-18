#!/usr/bin/python3

"""
module of a flask web application
"""


from flask import Flask

app = Flask(__name__)

app.url_map.strict_slashes = False


@app.route("/")
def hello():
    """
    Returns a string hello HBNB!
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hello_hbnb():
    """
    Returns string HBNB
    """
    return "HBNB"


@app.route("/c/<text>")
def dispaly_c_text(text):
    """
    Returns C followed by text variable value
    """
    text = text.replace('_', ' ')
    return "C {}".format(text)


@app.route("/python/")
@app.route("/python/<text>")
def python_text(text="is cool"):
    """
    return text with also default value
    """
    text = text.replace('_', ' ')
    return "Python {}".format(text)


@app.route("/number/<int:n>")
def is_number(n):
    """
    Returns if n is int else error
    """
    n = str(n)
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
