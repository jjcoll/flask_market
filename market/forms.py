from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired


# inherit from FlaskForm
class RegisterForm(FlaskForm):
    # form fields
    username = StringField(label="User Name:", validators=[Length(min=3, max=30)])
    email_address = StringField(
        label="Email Address:", validators=[Email(), DataRequired()]
    )
    password1 = PasswordField(
        label="Password:", validators=[Length(min=8), DataRequired()]
    )
    password2 = PasswordField(
        # verify that password and confirm password are same
        label="Confirm Password:",
        validators=[EqualTo("password1"), DataRequired()],
    )
    submit = SubmitField(label="Create Account")
