from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db


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


@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()

    return render_template("login.html", form=form)
