from sqlalchemy import create_engine

#in memory only sqlite db
engine = create_engine('sqlite:///:memory:', echo=True)

# Lazy Connecting
# The Engine, when first returned by create_engine(), has not actually tried to connect to the database yet; that happens only the first time it is asked to perform a task against the database.

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nickname = Column(String(50), unique=True)
    password = Column(String(50))
    email = Column(String(50))

    posts = pony.Set("Post")
    comments = pony.Set("Comment")
    replies = pony.Set("Reply")

    def __repr__(self):
        return '<User {}, with email: {}>'.format(self.nickname, self.email)


class Post(Base):

    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(Text)

    user_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))

    user = Relationship("User", backref=backref('users', order_by=id))
    comment = Relationship("Comment", backref=backref('comments', order_by=id))
    

    def __repr__(self):
        return '<Post {}, with title "{}">'.format(self.id, self.title)


class Comment(Base):

    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)

    title = Column(String(255))
    body = Column(Text)

    user = pony.Required(User)
    post = pony.Required(Post)

    replies = pony.Set("Reply")

    def __repr__(self):
        return '<Comment {}, with title "{}">'.format(self.id, self.title)


class Reply(Base):

    __tablename__ = 'replies'
    id = Column(Integer, primary_key=True)

    body = Column(Text)

    user = pony.Required(User)
    comment = pony.Required(Comment)

    def __repr__(self):
        return 'Reply {}, to comment {}'.format(self.id, self.comment)

