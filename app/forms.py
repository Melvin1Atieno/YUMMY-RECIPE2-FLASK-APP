
from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import ValidationError, InputRequired, Email,EqualTo
from app.models import User




class SignupForm(Form):
    firstname  = StringField(label="First Name: ",description="First name", validators=[InputRequired("*")])
    lastname = StringField(label="Last Name: ", description="last name", validators=[InputRequired("*")])
    email = EmailField(label="Email: ", description="Email address", validators=[InputRequired("*"),Email()])
    username = StringField(label="User Name :",description="Username", validators=[InputRequired("*")])
    password = PasswordField(label="Password :",description="Enter password", validators=[InputRequired("*")])
    confirmpassword = PasswordField(label="Confirm Password",description="confirm password",validators=[InputRequired("*"),EqualTo("password",("password must be the same"))])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField("Sign In") 

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError("Username already taken.")
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError("Email already registered to an existing account. ")
class LoginForm(SignupForm):
    username = StringField(label="User Name :",description="Username", validators=[InputRequired("*")])
    password = PasswordField(label="Password :",description="Enter password", validators=[InputRequired("*")])
    remember_me = BooleanField(label="Remember Me")
    submit = SubmitField("Sign In") 
