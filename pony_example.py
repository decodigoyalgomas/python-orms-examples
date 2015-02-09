import pony.orm as pony
import os


basedir = os.path.abspath(os.path.dirname(__file__))
PONY_DATABASE_URI = os.path.join(basedir, 'weddings.db')

database = pony.Database(
    "sqlite",
    PONY_DATABASE_URI,
    create_db=True
)

class User(database.Entity):
    """User, it is asociated with the posts, comments and replies he makes"""

    nickname = pony.Required(unicode, unique=True)
    password = pony.Required(unicode)
    email = pony.Required(unicode, unique=True)

    posts = pony.Set("Post")
    comments = pony.Set("Comment")
    replies = pony.Set("Reply")

    def __repr__(self):
        return '<User {}, with email: {}>'.format(self.nickname, self.email)


class Post(database.Entity):

    title = pony.Required(unicode)
    body = pony.Required(unicode)

    user = pony.Required(User)

    comments  = pony.Set("Comment")

    def __repr__(self):
        return '<Post {}, with title "{}">'.format(self.id, self.title)

class Comment(database.Entity):

    title = pony.Required(unicode)
    body = pony.Required(unicode)

    user = pony.Required(User)
    post = pony.Required(Post)

    replies = pony.Set("Reply")

    def __repr__(self):
        return '<Comment {}, with title "{}">'.format(self.id, self.title)


class Reply(database.Entity):

    body = pony.Required(unicode)

    user = pony.Required(User)
    comment = pony.Required(Comment)

    def __repr__(self):
        return 'Reply {}, to comment {}'.format(self.id, self.comment)

