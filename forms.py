from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField, FileField
from wtforms.validators import InputRequired, Email, Length, Optional

class UserAddForm(FlaskForm):
    """Form for adding a user."""
    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=20)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=6, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    image_url = StringField('Image URL', validators=[Optional()])
    submit = SubmitField('Sign Up')

class UserEditForm(FlaskForm):
    """Form for editing a user."""
    username = StringField('Username', validators=[InputRequired(), Length(min=1, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    image_url = StringField('Image URL', validators=[Optional()])
    header_image_url = StringField('Header Image URL', validators=[Optional()])
    bio = TextAreaField('Bio', validators=[Optional()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Save Changes')

class LoginForm(FlaskForm):
    """Form for user login."""
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Log In')

class MessageForm(FlaskForm):
    """Form for adding a message."""
    text = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Send') 