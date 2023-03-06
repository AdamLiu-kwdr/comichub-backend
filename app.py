from flask import Flask
from flask_migrate import Migrate, upgrade
from models import db
from comic_api import comic_api

app = Flask(__name__)

#TODO: read database connection string from env
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///:memory:" 
app.config["SQLALCHEMY_ECHO"] = "True"

app.register_blueprint(comic_api)

migrate = Migrate(app, db)

db.init_app(app)

with app.app_context():
    # !!! AUTO MIGRATE !!! Only enable this line in debug mode
    upgrade(directory='migrations', revision='head')