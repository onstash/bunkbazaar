from flask.ext.wtf import Form
from wtforms.fields import TextField,TextAreaField,SubmitField
from wtforms.validators import DataRequired, ValidationError

class ContactForm(Form):
	name = TextField("Name", validators=[DataRequired()])
	email = TextField("Email", validators=[DataRequired()])
	subject = TextField("Subject", validators=[DataRequired()])
	message = TextAreaField("Message", validators=[DataRequired()])
	submit = SubmitField("Send")
