from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, length

class RegistrationForm(FlaskForm):
    name=StringField("Full name", validators=[DataRequired()])
    email=StringField("Email", validators=[DataRequired(), Email()])
    password=PasswordField("Password", validators=[DataRequired(),length(min=6)])
    submit=SubmitField("Register")