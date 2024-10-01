import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or "postgresql://user:password@hostname:port/dbname"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
