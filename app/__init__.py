from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager

# make app an instance of the class Flask
app = Flask(__name__)

login = LoginManager(app)
app.config.from_object(Config)
# __name__ python predefined variable, set to the name of the module in which it is used
# db object that represents the database
db = SQLAlchemy(app)
# migrate object that represents the migration engine
migrate = Migrate(app, db)

# import the model module to represent database structure
from app import routes, models