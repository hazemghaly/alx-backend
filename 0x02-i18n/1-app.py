#!/usr/bin/env python3
"""basic flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configurations for the Flask app."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route("/")
def home():
    """home function define yor title and header"""
    return render_template("0-index.html", title="“Welcome to Holberton")
