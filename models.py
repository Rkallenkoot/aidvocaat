from config import app, db

class Chat(db.Model):
	chat_id = db.Column(db.Integer, primary_key=True)
	case_id = db.Column(db.Integer, nullable=False)
	agent = db.Column(db.Integer, nullable=False)
	content = db.Column(db.String, nullable=False)

with app.app_context():
	db.create_all()

