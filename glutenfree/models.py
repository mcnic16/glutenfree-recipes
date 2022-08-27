from glutenfree import db

class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisine_type = db.Column(db.Text, unique=True, nullable=False)
    cuisine_name = db.Column(db.Text, unique=True, nullable=False)
    cuisine_tools = db.Column(db.Text, unique=True, nullable=False)
    cuisine_ingredients = db.Column(db.Text, unique=True, nullable=False)
    cuisine_directions = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"Cuisine('{self.id}', '{self.cuisine_name}', \
        '{self.cuisine_type},\
        '{self.scuisine_tools}', '{self.cuisine_ingredients}', \
        '{self.scuisine_directions}')"


