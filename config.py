import os
basedir = os.path.abspath(os.path.dirname(__file__)) 


class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///"+ os.path.join(basedir, "app.db")
    # disables the configurationoption that signals the application everytime a change
    # is about to be made in the database
    SQLALCHEMY_TRACK_MODIFICATIONS = True
