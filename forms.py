from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Email, EqualTo
from config import db
from datetime import date

class ChatForm(FlaskForm):
	content = StringField('content', validators = [InputRequired()], render_kw={"placeholder": "Search case"})
