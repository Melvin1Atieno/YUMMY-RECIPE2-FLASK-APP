from flask import Flask

# make app an instance of the class Flask
app = Flask(__name__)
# __name__ python predefined variable, set to the name of the module in which it is used

from app import routes