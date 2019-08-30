import os
from flask import Flask
from config import Config
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

toolbar = DebugToolbarExtension()
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app(test_config=None):
	# create an configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.debug = True
	app.config.from_object(Config)

	toolbar.init_app(app)
	db.init_app(app)
	migrate.init_app(app, db)
	login.init_app(app)

	from . import main
	app.register_blueprint(main.bp)

	from . import store
	app.register_blueprint(store.bp)

	from . import auth
	app.register_blueprint(auth.bp)

	from . import admin
	app.register_blueprint(admin.bp)

	login.login_view = 'auth.login'

	return app

from . import models