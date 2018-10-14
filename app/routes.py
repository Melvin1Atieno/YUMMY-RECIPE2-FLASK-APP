from flask import render_template, redirect, url_for,flash,request
from werkzeug.urls import url_parse
from app import app
from app import db
from app.forms import SignupForm,LoginForm
from flask_login import current_user, login_user,login_required

from app.models import User


# @app.route("/index")
# def index():
#     return render_template("index.html"), 200

@app.route("/", methods=["GET","POST"])
@app.route('/signup', methods=['GET','POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            firstname= form.firstname.data,
            lastname =form.lastname.data,
            email = form.email.data,
            username = form.username.data,
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Success")
        return redirect(url_for('login'))
    return render_template('index.html',form=form)

@app.route('/login', methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or Password")
            return redirect(url_for("index"))
        login_user(user,remember=form.remember_me.data)
        # next_page = request.args.get('next')
        # if not next_page or url_parse(next_page).netloc != '':
        #     next_page = url_for('index')
        return redirect(url_for('home'))
    return render_template("index.html",form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))




@app.route('/home',methods=["GET","POST"])
@login_required
def home():
    return render_template("homepage.html")





