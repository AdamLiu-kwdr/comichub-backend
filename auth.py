from sqlalchemy import select
from app import jwt
from models import User, db


@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.id


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return db.session.scalars(select(User).where(User.id == identity)).one_or_none()
