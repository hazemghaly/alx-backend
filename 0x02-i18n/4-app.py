#!/usr/bin/env python3
"""detect if the incoming request contains locale argument
and ifs value is a supported locale,
return it. If not or if the parameter is not present,
resort to the previous default behavior.
"""

from flask import Flask, render_template, session, request
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


@babel.localeselector
def get_locale() -> str:
    """determine language"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def home() -> str:
    '''
    Render the home page with translated title and header.
    
    '''
    title = _('home_title')
    header = _('home_header')
    return render_template("4-index.html", title=title, header=header)


# babel.init_app(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run()
