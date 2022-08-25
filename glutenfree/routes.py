from flask import render_template
from glutenfree import app, db
from glutenfree import Starters, Mains, Desserts, Drinks, Cuisine



@app.route("/")
def home():
    return render_template("base.html")