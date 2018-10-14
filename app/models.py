from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login
# inherits from the db.Model class, a base class for all models from Flask-SQLAlchemy

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(32), index=True, unique=True)
    lastname = db.Column(db.String(32), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    recipe = db.relationship("Recipe", backref="author", lazy="dynamic")
#     def set_password(self,password):
#         self.password_hash = generate_password_hash(password)
    
#     def check_password(self, password):
#         return check_password_hash(self.password_hash, password)
# # __repr__  a method that tells python how to print objects usefull for debugging
    def __repr__(self):
        return "<user {}>".format(self.username)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipename = db.Column(db.String(140), index=True)
    ingredients = db.Column(db.String(140))
    method = db.Column(db.String(140))
    category = db.Column(db.String(32), index=True)
    timestamp = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


    def __repr__(self):
        return "<Recipe {} {} {} {}>".format(self.recipename, self.category,self.ingredients, self.method, )
