#!/usr/bin/env python3
"""basic flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)


@app.route("/")
def home():
    """home function define yor title and header"""
    return render_template("0-index.html", title="“Welcome to Holberton")
