from flask import render_template, redirect, url_for,flash
from app import app
from app.forms import LoginForm,SignupForm
from flask_login import current_user, login_user
from app.models import User

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    # form = LoginForm()
    form = SignupForm()
    if form.validate():
        return redirect("/index")
    return render_template("index.html", form=form), 200

@app.route('/login', methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    forml = LoginForm()
    form.username
    if loginform.validate_on_submit():
        user = User.query.filter_by(username=loginform.username.data).first()
        if user is None or not user.check_password(loginform.password.data):
            flash("Invalid username or Password")
            return redirect(url_for("index"))
        login_user(user,remember=loginform.remember_me.data)
        return redirect(url_for("index"))
    return render_template("index.html",form=loginform)





