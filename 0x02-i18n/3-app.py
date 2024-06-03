#!/usr/bin/env python3
"""detect if the incoming request contains locale argument
and ifs value is a supported locale,
return it. If not or if the parameter is not present,
resort to the previous default behavior.
"""

from flask import Flask, render_template, session, request
from flask_babel import Babel
# from flask_babel import gettext as _

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
    determine language
    you should be able to test different translations

    Returns:
        str: best match
    '''
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home():
    '''
    home function define yor title and header

    Rerturn
        3-index
    '''
    return render_template("3-index.html")
