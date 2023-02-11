import openai
from flask import session, redirect, render_template, request, url_for, abort
from forms import ChatForm
from dateutil import parser
from config import app, db
from models import Chat
from tempfile import NamedTemporaryFile

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/docs")
def docs():
	return render_template("docs.html")

@app.route("/notes")
def notes():
	return render_template("notes.html")


CHATGPT = 0
USER = 1
######################
#        CHAT        #
######################
with app.app_context():
	if (Chat.query.count() == 0):
		chat = Chat(
			chat_id = 0, 
			case_id = 1, 
			agent = CHATGPT,
			content = "Start of your conversation"
		)
		db.session.add(chat)
		try:
			db.session.commit()
		except Exception as e:
			print(e)
			db.session.rollback()
		finally:
			db.session.close()

@app.route("/chat/<int:id>", methods=("GET", "POST"))
def chat(id):
	form = ChatForm()
	if request.method == "POST":
		new_question = Chat(
			chat_id = Chat.query.count()+1,
			case_id = id,
			agent = USER,
			content = request.form["content"]
		)
		addChatToDatabase(new_question)

		new_reply = Chat(
			chat_id = Chat.query.count()+1,
			case_id = id,
			agent = CHATGPT,
			content = createChatResponse(request.form["content"])
		)
		addChatToDatabase(new_reply)

		chats = Chat.query.filter_by(case_id = id)
		if form.validate_on_submit():
			return render_template("chat.html", form = form, chats = chats, case_id=id)
		else:
			print (form.errors)
	chats = Chat.query.filter_by(case_id = id)
	return render_template("chat.html", form = form, chats = chats, case_id=id)

def addChatToDatabase(new_chat):
	db.session.add(new_chat)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
	finally:
		db.session.close()

def createChatResponse(input):
	response = openai.Completion.create(
		# model="text-davinci-003",
		# model="text-curie-001",
		model="text-babbage-001",
		prompt=generate_prompt(input),
		temperature=0.9,
		max_tokens=150,
		top_p=1.0,
		frequency_penalty=0.0,
		presence_penalty=0.6,
		best_of=1
	)
	return response.choices[0].text

def generate_prompt(input):
	return "Human: " + input + "\n AI:"
