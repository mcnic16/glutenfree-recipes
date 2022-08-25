from glutenfree import db


Class Starters(db.Model):
    # schema for Starters
    id = db.Column(db.integer, primary_key=True)
    starters_name = db.column(db.text, unique=True, nullable=False)
    starters_tools = db.column(db.text, unique=True, nullable=False)
    starters_ingredients = db.column(db.text, unique=True, nullable=False)
    starters_directions = db.column(db.text, unique=True, nullable=False)
    
    def __repr__(self):
        return f"Starters('{self.id}', '{self.starters_name}', '{self.starters_tools}',
        '{self.starters_ingredients}', '{self.starters_directions}')"


Class Mains(db.Model):
    # schema for Mains
    id = db.Column(db.integer, primary_key=True)
    mains_name = db.column(db.text, unique=True, nullable=False)
    mains_tools = db.column(db.text, unique=True, nullable=False)
    mains_ingredients = db.column(db.text, unique=True, nullable=False)
    mains_directions = db.column(db.text, unique=True, nullable=False)

    def __repr__(self):
        return f"Mains('{self.id}', '{self.mains_name}', '{self.mains_tools}',
        '{self.mains_ingredients}', '{self.mains_directions}')"


Class Desserts(db.Model):
    # schema for Desserts
    id = db.Column(db.integer, primary_key=True)
    desserts_name = db.column(db.text, unique=True, nullable=False)
    desserts_tools = db.column(db.text, unique=True, nullable=False)
    desserts_ingredients = db.column(db.text, unique=True, nullable=False)
    desserts_directions = db.column(db.text, unique=True, nullable=False)

    def __repr__(self):
        return f"Desserts('{self.id}','{self.desserts_name}', '{self.desserts_tools}',
        '{self.desserts_ingredients}', '{self.dessert_directions}')"


Class Drinks(db.Model):
    # schema for Cuisine
    id = db.Column(db.integer, primary_key=True)
    drinks_name = db.column(db.text, unique=True, nullable=False)
    drinks_tools = db.column(db.text, unique=True, nullable=False)
    drinks_ingredients = db.column(db.text, unique=True, nullable=False)
    drinks_directions = db.column(db.text, unique=True, nullable=False)

    def __repr__(self):
        return f"Drinks('{self.id}', '{self.drinks_name}', '{self.drinks_tools}', 
        '{self.drinks_ingredients}', '{self.drinks_directions}')"


Class Cuisine(db.Model):
     # schema for Cuisine
    id = db.Column(db.integer, primary_key=True)
    starters_id = db.Column(db.Integer, db.ForeignKey("starters.id", ondelete="CASCADE"), nullable=False)
    mains_id = db.Column(db.Integer, db.ForeignKey("mains.id", ondelete="CASCADE"), nullable=False)
    desserts_id = db.Column(db.Integer, db.ForeignKey("desserts.id", ondelete="CASCADE"), nullable=False)
    drinks_id = db.Column(db.Integer, db.ForeignKey("drinks.id", ondelete="CASCADE"), nullable=False)
    starters = db.relationship("Starter", backref="cuisine", cascade="all, delete", lazy=True)
    mains = db.relationship("Mains", backref="cuisine", cascade="all, delete", lazy=True)
    desserts = db.relationship("Desserts", backref="cuisine", cascade="all, delete", lazy=True)
    drinks = db.relationship("Drinks", backref="cuisine", cascade="all, delete", lazy=True)


    def __repr__(self):
        return f"Cuisine('{self.id}', '{self.starters_id}', '{self.mains_id}', '{self.desserts_id}',
        '{self.drinks_id}', '{self.starters}', '{self.mains}, '{self.desserts}', '{self.drinks}')"



