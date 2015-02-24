import pony.orm as pony

from models import User, Post, Comment, Reply



def printUsers():
	""" Imprimimos en pantalla todos los objetos user de la BBDD """
	with pony.db_session:
	    users = pony.select(user for user in User)
	    for user in users:
	        print user

def getUserById(_id):
	""" Imprimimos en pantalla el objeto User seleccionado por su id """
	with pony.db_session:
		user = User.get(id=_id)
		print user

def getUserPosts(user):
	""" Imprimimos en pantalla todos los objetos Post del user con el Id especificado """
	with pony.db_session:
		posts = pony.select(post for post in Post if post.user.id == user)
		for post in posts:
			print post


def getComments(user):
	""" Imprime todos los objetos comment del user con el ID especificado """
	with pony.db_session:
		comments = Comment.select_by_sql("SELECT * FROM comment WHERE user = " + str(user) )
		for comment in comments:
			print comment

def limitReplies(limit):
	""" Imprime el numero de replies pasado como argumento y ordenalos segun el User que los creó """
	with pony.db_session:
		replies = pony.select(reply for reply in Reply).order_by(Reply.user).limit(limit)

		for reply in replies:
			print reply