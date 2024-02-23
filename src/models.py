import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(100), nullable=False)
    email = Column(String(50), nullable=False, unique=True)


class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("users.id"))
    user_from = relationship(Users)
    user_to_id = Column(Integer, ForeignKey("users.id"))
    user_to = relationship(Users)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(Users)


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(300), nullable=False)
    author_id = Column(Integer, ForeignKey("users.id"))
    users = relationship(Users)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(Enum, nullable=False)
    url = Column(String(250), nullable=True)
    post_id = Column(Integer, ForeignKey("post.id"))
    post = relationship(Post)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
