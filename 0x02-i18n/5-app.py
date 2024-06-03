#!/usr/bin/env python3
"""basic flask app
"""
from typing import (
    Dict, Union
)
from flask import Flask, render_template, session, request, g
from flask_babel import Babel, get_locale
# from flask_babel import gettext as _


app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configurations for the Flask app."""
    DEBUG = True
    BABEL_TRANSLATION_DIRECTORIES = 'translations'
    LANGUAGES = ["en", "fr"]
    local_lang = 'en'
    TIMEZONE = 'UTC'


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieves a user based on a user id.
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """

    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    '''
    determine language
    you should be able to test different translations

    Returns:
        str: best match
    '''
    locale = request.args.get('locale', '').strip()
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    ''''
    home function define yor title and header

    Returns:
        html: homepage
    '''
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
