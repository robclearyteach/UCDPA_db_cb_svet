from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    """
    Model for storing user information.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the user
    username = db.Column(db.String(150), unique=True, nullable=False)  # Username, must be unique and not nullable
    email = db.Column(db.String(150), unique=True, nullable=False)  # Email, must be unique and not nullable
    password = db.Column(db.String(150), nullable=False)  # Password, not nullable

    def __repr__(self):
        return f"<User {self.username}>"

class Recipe(db.Model):
    """
    Model for storing recipe information.
    """
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for the recipe
    title = db.Column(db.String(255), nullable=False, unique=True, index=True)  # Recipe title, must be unique, not nullable, and indexed for faster searches
    ingredients = db.Column(db.Text, nullable=False)  # Ingredients for the recipe, not nullable
    instructions = db.Column(db.Text, nullable=False)  # Instructions for the recipe, not nullable
    image_name = db.Column(db.String(255), default='default_image.jpg')  # Image name for the recipe, defaults to 'default_image.jpg' if not provided

    def __repr__(self):
        return f"<Recipe {self.title}>"
