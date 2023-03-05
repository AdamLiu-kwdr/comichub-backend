from flask import Flask
from models import db
from comic_api import comic_api

app = Flask(__name__)

#TODO: remove this stub start up section
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///:memory:" 

app.register_blueprint(comic_api)

db.init_app(app)

#TODO: move to migrate based
with app.app_context():
    db.create_all()