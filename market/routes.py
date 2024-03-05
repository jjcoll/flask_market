from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template("market.html", items=items)


@app.route("/register", methods=["POST", "GET"])
def register_page():
    form = RegisterForm()

    # on submit checks that the user clicks on submit button
    # also checks for validation
    if form.validate_on_submit():
        # passing fields from form
        user_to_create = User(
            username=form.username.data,
            email=form.email_address.data,
            # this executes the password setter
            password=form.password1.data,
        )
        # submit changes to data base
        db.session.add(user_to_create)
        # save changes to data base
        db.session.commit()
        # redirect user to market
        return redirect(url_for("market_page"))

    # check for errors arriving from validations
    if form.errors != {}:  # if there are no errors from validation
        for err_msg in form.errors.values():
            flash(
                f"There was an error in the user creation: {err_msg}", category="danger"
            )  # print in server side

    return render_template("register.html", form=form)


@app.route("/login", methods=["POST", "GET"])
def login_page():
    form = LoginForm()

    if form.validate_on_submit():
        # filter user by username
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            form.password.data
        ):
            login_user(attempted_user)
            flash(
                f"Success! You are logged in as {attempted_user.username}",
                category="success",
            )
            return redirect(url_for("market_page"))
        else:
            flash(
                f"User and password do not match! Please try again", category="danger"
            )

        # verify if the password is correct

    return render_template("login.html", form=form)
