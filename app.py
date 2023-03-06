from flask import Flask
from flask_jwt_extended import JWTManager
from models import db, User
from comic_api import comic_api
from auth_api import auth_api

app = Flask(__name__)

#TODO: remove this stub start up section
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite+pysqlite:///:memory:" 
app.config["SQLALCHEMY_ECHO"] = "True"

app.register_blueprint(comic_api, url_prefix='/comic')
app.register_blueprint(auth_api)

db.init_app(app)

app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)

#TODO: move db to migrate based, GENERATE ADMIN ACCOUNT'S PASSWORD FROM ENV!
with app.app_context():
    db.create_all()

    admin = User(name = "admin")
    admin.modify_password_hash("admin_password")
    db.session.add(admin)
    db.session.commit()