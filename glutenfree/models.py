from glutenfree import db

class Cuisine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cuisine_type = db.Column(db.Text, unique=True, nullable=False)
    cuisine_name = db.Column(db.Text, unique=True, nullable=False)
    cuisine_tools = db.Column(db.Text, unique=True, nullable=False)
    cuisine_ingredients = db.Column(db.Text, unique=True, nullable=False)
    cuisine_directions = db.Column(db.Text, unique=True, nullable=False)

    def __repr__(self):
        return f"Cuisine('{self.id}', '{self.starters_name}', \
        '{self.starters_tools}', '{self.starters_ingredients}', \
        '{self.starters_directions}')"


class Starters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    starters = db.relationship("Cuisine", backref="cuisine", cascade="all, delete", lazy=True)
    starters_id = db.Column(db.Integer, db.ForeignKey("cuisine.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"Starters('{self.id}', '{self.starters}', \
            '{self.starters_id}')"


class Mains(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mains = db.relationship("Cuisine", backref="cuisine", cascade="all, delete", lazy=True)
    mains_id = db.Column(db.Integer, db.ForeignKey("cuisine.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"Mains('{self.id}', '{self.mains}', \
            '{self.mains_id}')"


class Desserts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    desserts = db.relationship("Cuisine", backref="cuisine", cascade="all, delete", lazy=True)
    desserts_id = db.Column(db.Integer, db.ForeignKey("cuisine.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"Desserts('{self.id}', '{self.desserts}', \
            '{self.desserts_id}')"


class Drinks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    drinks = db.relationship("Cuisine", backref="cuisine", cascade="all, delete", lazy=True)
    drinks_id = db.Column(db.Integer, db.ForeignKey("cuisine.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        return f"Drinks'{self.id}', '{self.drinks}', \
            '{self.drinks_id}')"
