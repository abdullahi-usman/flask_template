
import os

from flask import Flask, render_template

from . import db


def create_app(**test_config):
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(SECRET_KEY='dev', DATABASE=os.path.join(app.instance_path, 'flask.sqlite'))
    
    if test_config is None:
        app.config.from_pyfile('config.py', True)
    else:
        app.config.from_mapping(test_config)
    
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/')
    def index():
        return render_template('index.html')

    db.init_app(app)

    return app