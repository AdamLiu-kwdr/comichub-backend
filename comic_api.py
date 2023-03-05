from datetime import datetime
from flask import Blueprint, jsonify, request, abort
from models import db, Comic, Page
from sqlalchemy import select

comic_api = Blueprint("comic_api", __name__)


@comic_api.get('/')
def get_all():
    comics = db.session.scalars(
        select(Comic).order_by(Comic.publish_date)).all()
    return jsonify(comics)


@comic_api.get('/<id>')
def get_by_id(id):
    comic = db.get_or_404(Comic, id)
    return jsonify(comic)


@comic_api.post('/')
def create_comic():
    request_json = request.get_json()
    new_comic = Comic(
        name=request_json['name'],
        description=request_json['description'],
        publish_date=datetime.now()
    )
    db.session.add(new_comic)
    db.session.commit()
    return jsonify(new_comic)


@comic_api.put('/')
def update_comic():
    request_json = request.get_json()
    if 'id' in request_json:
        modify_commic: Comic = db.get_or_404(Comic, request_json['id'])
        modify_commic.name = request_json['name']
        modify_commic.description = request_json['description']
        modify_commic.update_date = datetime.now()
        db.session.add(modify_commic)
    else:
        modify_commic = Comic(
            name=request_json['name'],
            description=request_json['description'],
            publish_date=datetime.now()
        )
        db.session.add(modify_commic)

    db.session.commit()
    return jsonify(modify_commic)


@comic_api.delete('/<id>')
def delete_comic(id):
    comic: Comic = db.get_or_404(Comic, id)
    db.session.delete(comic)
    db.session.commit()
    return 200
