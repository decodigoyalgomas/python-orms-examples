import pony.orm as pony

from models import User, Post, Comment, Reply


@pony.db_session
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

if __name__ == '__main__':
	add_data()