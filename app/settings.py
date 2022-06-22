import os

from sqlalchemy import false

MONGO_URI = os.getenv("MONGO_URI")
SECRET_KEY = os.getenv("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = false