#!/usr/bin/env python3
"""basic flask app
"""

from flask import Flask, render_template, session, request
from flask_babel import Babel
from flask_babel import gettext as _

app = Flask(__name__)

babel = Babel(app)


class Config:
    '''
    Configurations for the Flask app.
    '''
    LANGUAGES = ["en", "fr"]
    local_lang = 'en'
    TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    '''
    Gets locale from request object
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    '''
    home function define yor title and header
    '''
    title = _("home_title")
    header = _("home_header")

    return render_template("3-index.html", title=title, header=header)
