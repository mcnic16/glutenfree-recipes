from flask import render_template
from glutenfree import app, db
from glutenfree.models import Cuisine, Starters



@app.route("/")
def home():
    return render_template("cuisine.html")



