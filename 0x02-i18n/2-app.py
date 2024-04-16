#!/usr/bin/env python3
"""basic flask app
"""

from flask import Flask, render_template, session, request
from flask_babel import Babel


app = Flask(__name__)

babel = Babel(app)


class Config:
    """Configurations for the Flask app."""
    LANGUAGES = ["en", "fr"]
    local_lang = 'en'
    TIMEZONE = 'UTC'


app.config.from_object(Config)

# @app.route('/language/<language>')
# def set_language(language=None):
#     session['language'] = language
#     return redirect(url_for('index'))


@babel.localeselector
def get_locale():
    """determine language"""
    try:
        language = session['language']
    except KeyError:
        language = None
    if language is not None:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())

# babel = Babel(app, locale_selector=get_locale)

# @app.context_processor
# def inject_conf_var():
#     return dict(
#         AVAILABLE_LANGUAGES=app.config['LANGUAGES'],
#         CURRENT_LANGUAGE=session.get(
#             'language',request.accept_languages.best_match(
#                 app.config['LANGUAGES'].keys())))


@app.route("/")
def home():
    """home function define yor title and header"""
    return render_template("2-index.html", title="“Welcome to Holberton")
