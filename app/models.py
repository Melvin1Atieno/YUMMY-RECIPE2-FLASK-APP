from app import db
import datetime

# inherits from the db.Model class, a base class for all models from Flask-SQLAlchemy
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    # recipes = db.relationship("Recipe", backref="author", lazy="dynamic")

# __repr__  a method that tells python how to print objects
    def __repr__(self):
        return "<user {}>".format(self.username)

class RecipeCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String(140))
    recipes = db.relationship("Recipe", backref="category", lazy="dynamic")

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
