from typing import Optional
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from sqlalchemy import select
from models import db, User

auth_api = Blueprint("auth_api",__name__)

@auth_api.post('/login')
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user: Optional[User] = db.session.scalars(select(User).where(User.name == username)).one_or_none()
    if not user or not user.check_password(password):
        return jsonify("User does not exits or incorrect password"), 401

    access_token = create_access_token(identity=user)
    return jsonify(access_token=access_token)