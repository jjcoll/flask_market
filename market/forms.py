from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


# inherit from FlaskForm
class RegisterForm(FlaskForm):

    # flask knows to "validate" the field "username", so name must be like this
    def validate_username(self, username_to_check):

        # check if user already exists
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError(
                "Username already exists! Please try a different username."
            )

    def validate_email_address(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("Email already in use! Please try a different Email.")

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


class LoginForm(FlaskForm):
    username = StringField(label="User Name:", validators=[DataRequired()])
    password = PasswordField(label="Password:", validators=[DataRequired()])
    submit = SubmitField(label="Sign in")
