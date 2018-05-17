from flask import render_template, redirect
from app import app
from app.forms import LoginForm

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect("/index")
    return render_template("index.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)