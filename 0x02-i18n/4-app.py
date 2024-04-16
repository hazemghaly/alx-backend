#!/usr/bin/env python3
"""detect if the incoming request contains locale argument
and ifs value is a supported locale,
return it. If not or if the parameter is not present,
resort to the previous default behavior.
"""

from flask import Flask, render_template, session, request
from flask_babel import Babel
from flask_babel import gettext as _


app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configurations for the Flask app."""
    LANGUAGES = ["en", "fr"]
    local_lang = 'en'
    TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """determine language"""
    locale_p = request.args.get('locale')
    if locale_p and locale_p in app.config['LANGUAGES']:
        return locale_p
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def home():
    """home function define yor title and header"""
    title = _("home_title")
    header = _("home_header")

    return render_template("4-index.html", title=title, header=header)
