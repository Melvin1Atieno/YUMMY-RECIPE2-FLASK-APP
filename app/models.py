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
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # recipes = db.relationship("Recipe", backref="author", lazy="dynamic")
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
# __repr__  a method that tells python how to print objects
    def __repr__(self):
        return "<user {}>".format(self.username)

class RecipeCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String(140))
    recipes = db.relationship("Recipe", backref="recipecategory", lazy="dynamic")

    def __repr__(self):
        return "<Category {}>".format(self.categoryname)


class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipename = db.Column(db.String(140))
    ingredients = db.Column(db.String(140))
    method = db.Column(db.String(140))
    category = db.Column(db.Integer, db.ForeignKey("recipe_category.id"))
    timestamp = db.Column(db.DateTime, index=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


    def __repr__(self):
        return "<Recipe {} {} {} {}>".format(self.recipename, self.recipe_category,self.ingredients, self.method, )
