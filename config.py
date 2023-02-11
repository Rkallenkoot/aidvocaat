import os
import openai
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
with app.app_context():
	app.config['SECRET_KEY'] = 'dfewfew123213rwdsgert34tgfd1234trgf'
	app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
	openai.api_key = os.getenv("OPENAI_API_KEY")
	db = SQLAlchemy(app)
