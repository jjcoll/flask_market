from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# Construct the path to the database file inside the 'market' package
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
# secret key
app.config["SECRET_KEY"] = "5a7dc285da89f961bca6df365cee76bcb8b37dd5d650"
db = SQLAlchemy(app)

from market import routes


# with app.app_context():

#     #     db.session.query(Item).delete()
#     #     db.create_all()
#     #     db.session.commit()
#     #     items = Item.query.all()
#     #     print(items)
#     for item in Item.query.all():
#         print(item.name)

#     # Filter for items that cost 500 dollars
#     for item in Item.query.filter_by(price=500):
#         print(item.name)
