from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List
from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import DefaultMeta
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()


@dataclass
class Comic(db.Model):
    __tablename__ = "comic"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    description: Mapped[Optional[str]]
    publish_date: Mapped[datetime]
    update_date: Mapped[Optional[datetime]]

    pages: Mapped[List["Page"]] = relationship(back_populates="comic")


@dataclass
class Page(db.Model):
    __tablename__ = "page"

    id: Mapped[int] = mapped_column(primary_key=True)
    comic_id: Mapped[int] = mapped_column(ForeignKey("comic.id"))
    file_path: Mapped[str]
    page_number: Mapped[int]

    comic: Mapped[Comic] = relationship(back_populates="pages")


@dataclass
class User(db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(256))
    hashed_password: Mapped[str]
    email: Mapped[Optional[str]]

    def check_password(self, password) -> bool:
        return check_password_hash(self.hashed_password, password)
    
    def modify_password_hash(self,password):
        self.hashed_password = generate_password_hash(password)
