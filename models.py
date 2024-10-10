from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    """User model."""
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_url = db.Column(db.String(200), default="/static/images/default-pic.png")
    header_image_url = db.Column(db.String(200), default="/static/images/warbler-hero.jpg")
    bio = db.Column(db.Text, default="")
    messages = db.relationship('Message', backref='user', cascade="all, delete-orphan")
    likes = db.relationship('Message', secondary='likes', backref='liked_users')

    @classmethod
    def signup(cls, username, password, email, image_url=None):
        """Sign up user."""
        hashed = generate_password_hash(password)
        user = cls(username=username, password=hashed, email=email, image_url=image_url)
        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Authenticate user."""
        user = cls.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            return user
        return False

class Message(db.Model):
    """Message model."""
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

class Likes(db.Model):
    """Likes model."""
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    message_id = db.Column(db.Integer, db.ForeignKey('messages.id'), nullable=False)