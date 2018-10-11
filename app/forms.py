
from wtforms import Form, StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, EqualTo


class LoginForm(Form):
    username = StringField(label="User Name :",description="Username", validators=[InputRequired()])
    password = PasswordField(label="Password :",description="Enter password", validators=[InputRequired()])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField("Sign In") 


class SignupForm(LoginForm):
    firstname  = StringField(label="First Name: ",description="First name", validators=[InputRequired()])
    lastname = StringField(label="Last Name: ", description="last name", validators=[InputRequired()])
    email = EmailField(label="Email: ", description="Email address", validators=[InputRequired()])
    confirmpassword = PasswordField(label="Confirm Password",description="confirm password",validators=[InputRequired(),EqualTo("password",("password must be the same"))])