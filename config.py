import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '12345')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class PostgreSQLConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:password@localhost/recipes')

class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///recipes.db'
