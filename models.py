from sqlalchemy import create_engine

#in memory only sqlite db
engine = create_engine('sqlite:///test.db', echo=True)

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

    posts = relationship("Post", order_by="Post.id", backref="user")
    comment = relationship("Comment", order_by="Comment.id", backref="user")
    replies = relationship("Reply", order_by="Reply.id", backref="user")

    def __repr__(self):
        return '<User {}, with email: {}>'.format(self.nickname, self.email)


class Post(Base):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))

    

    comments = relationship("Comment", order_by="Comment.id", backref="post")
    
    

    def __repr__(self):
        return '<Post {}, with title "{}">'.format(self.id, self.title)


class Comment(Base):

    __tablename__ = 'comments'

    id = Column(Integer, primary_key=True)

    title = Column(String(255))
    body = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))  
    post_id = Column(Integer, ForeignKey('posts.id'))

    

    replies = relationship("Reply", order_by="Reply.id", backref="comment")

    def __repr__(self):
        return '<Comment {}, with title "{}">'.format(self.id, self.title)


class Reply(Base):

    __tablename__ = 'replies'

    id = Column(Integer, primary_key=True)

    body = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    comment_id = Column(Integer, ForeignKey('comments.id'))  
    

    def __repr__(self):
        return 'Reply {}, to comment {}'.format(self.id, self.comment)


# Create all tables in the engine. This is equivalent to "Create Table"
#  statements in raw SQL.
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_data():

    new_user = User(
        nickname = "Dieguito",
        password = "mystrongpassword",
        email = "dieguito@athelas.pe"
    )

    new_user2 = User(
        nickname = "Ithilnaur",
        password = "mystrongpassword2",
        email = "ithilnaur@athelas.pe"
    )

    new_post = Post(
        title = "Como la vida misma",
        body="It's a dangerous business, Frodo, going out your door. You step onto the road, and if you don't keep your feet, there's no knowing where you might be swept off to.  ",
        user = new_user
    )

    new_comment = Comment(
        title = "Tu no sabes",
        body = "Roads go ever ever on,Over rock and under tree,By caves where never sun has shone,By streams that never find the sea;Over snow by winter sown,And through the merry flowers of June,Over grass and over stone, And under mountains in the moon.",
        user = new_user2,
        post = new_post
    )

    new_reply = Reply(
        body = "Some who have read the book, or at any rate have reviewed it, have found it boring, absurd, or contemptible, and I have no cause to complain, since I have similar opinions of their works, or of the kinds of writing that they evidently prefer.",
        user = new_user,
        comment = new_comment
    )

    session.add_all([new_user, new_user2, new_post, new_comment, new_reply])
    session.commit()


if __name__ == '__main__':
    add_data()