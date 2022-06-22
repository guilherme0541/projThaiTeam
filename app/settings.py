import os

from sqlalchemy import false

SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = false