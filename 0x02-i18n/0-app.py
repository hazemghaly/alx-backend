#!/usr/bin/env python3
"""basic flask app"""

from flask import Flask
from flask_babel import Babel


app = Flask(__name__)


@app.route("/")
def home():
    """home"""
    return "welcomehome"
