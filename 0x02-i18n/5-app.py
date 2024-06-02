#!/usr/bin/env python3
"""basic flask app
"""
from typing import (
    Dict, Union
)
from flask import Flask, render_template, session, request, g
from flask_babel import Babel, get_locale
from flask_babel import gettext as _


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


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    """
    Validate user login details
    Args:
        id (str): user id
    Returns:
        (Dict): user dictionary if id is valid else None
    """
    return users.get(int(id), 0)


@app.before_request
def load_user():
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        if user:
            g.user = user
        else:
            g.user = None
    else:
        g.user = None


@babel.localeselector
def get_locale() -> str:
    '''
    determine language
    you should be able to test different translations
    '''
    locale = request.args.get('locale', '').strip()
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    """home function define yor title and header"""
    title = _('home_title')
    header = _('home_header')
    return render_template("5-index.html", title=title, header=header)


if __name__ == "__main__":
    app.run()
