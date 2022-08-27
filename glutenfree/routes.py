from flask import render_template, request, redirect, url_for
from glutenfree import app, db
from glutenfree.models import Cuisine



@app.route("/")
def home():
    cuisine = list(Cuisine.query.order_by(Cuisine.id).all())
    return render_template("cuisine.html", cuisine=cuisine)


@app.route("/cuisine")
def cuisine():
    return render_template("cuisine.html", cuisine=cuisine)
    


@app.route("/addcuisine", methods=["GET", "POST"])
def addcuisine():
    if request.method == "POST":
        cuisine = Cuisine(
            cuisine_type = request.form.get("cuisine_type"),
            cuisine_name = request.form.get("cuisine_name"),
            cuisine_tools = request.form.get("cuisine_tools"),
            cuisine_ingredients = request.form.get("cuisine_ingredients"),
            cuisine_directions = request.form.get("cuisine_directions"),
        )
        db.session.add(cuisine)
        db.session.commit()
    
        return redirect(url_for("home"))
    return render_template("addcuisine.html")
