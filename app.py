from datetime import datetime
from flask import Flask
from flask_migrate import Migrate, upgrade
from models import db, Comic
from comic_api import comic_api
from sqlalchemy import insert
from flask_cors import CORS

app = Flask(__name__)
app.config.from_prefixed_env()

# TODO: read cors list from env
CORS(app)

app.register_blueprint(comic_api, url_prefix="/comic")

migrate = Migrate(app, db)

db.init_app(app)

with app.app_context():
    if app.config.get("AUTOMIGRATE") == "True":
        upgrade(directory='migrations', revision='head')

    if app.config.get("SEED_DEV_DATA") == "True":
        db.session.execute(
            insert(Comic),
            [
                {"name": "The adventure of meow", "description": "cat's adventure",
                    "publish_date": datetime.now()},
                {"name": "The roar of meow", "description": "cat's roar",
                    "publish_date": datetime.now()},
                {"name": "The purr of meow", "description": "cat's purring",
                    "publish_date": datetime.now()},
                {"name": "The adventure of meow vol.2",
                    "description": "cat's adventure 2", "publish_date": datetime.now()}

            ]
        )
        db.session.commit()
        db.session.close()
