# -*- coding: utf-8 -*-

from models import User, Post, Comment, Reply, session
from sqlalchemy.sql import text

def printUsers():
    """ Imprimimos en pantalla todos los objetos user de la BBDD """

    users = session.query(User).all()
    for user in users:
        print user


def getUserById(_id):
    """ Imprimimos en pantalla el objeto User seleccionado por su id """
    user =  session.query(User).filter_by(id=_id).one()
    print user


def getUserPosts(_id):
    """ Imprimimos en pantalla todos los objetos Post del user con el Id especificado """
    user =  session.query(User).filter_by(id=_id).one()
    for post in user.posts:
        print post


def getComments(user):
    """ Imprime todos los objetos comment del user con el ID especificado """
    comments = session.query(User).from_statement(
        text("SELECT * FROM comments WHERE user_id = {}".format(user))
    )  
    for comment in comments:
        print comment


def limitReplies(limit):
    """ Imprime el numero de replies pasado como argumento y ordenalos segun el User que los creó """
    replies = session.query(Reply).order_by(Reply.user_id)[0:limit]
    for reply in replies:
        print reply
