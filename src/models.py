from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    

    def __repr__(self):
        return self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rotation_period= db.Column(db.String(250))
    orbital_period= db.Column(db.String(250))
    diameter= db.Column(db.String(250))
    climate= db.Column(db.String(250))
    gravity= db.Column(db.String(250))
    terrain= db.Column(db.String(250))
    surface_water = db.Column(db.String(250))
    population = db.Column(db.String(250))


    def __repr__(self):
        return self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "population":self.population,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    mass = db.Column(db.String(250))
    hair_color = db.Column(db.String(250))
    skin_color = db.Column(db.String(250))
    eye_color = db.Column(db.String(250))
    birth_year = db.Column(db.String(250))
    gender = db.Column(db.String(250))
    homeworld_id = db.Column(db.Integer,db.ForeignKey("planets.id"))
    homeworld = db.relationship('Planets')
    

    

    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id":self.id,
            "name":self.name,
            "height":self.height,
            "mass":self.mass,
            "hair_color":self.hair_color,
            "skin_color":self.skin_color,
            "eye_color":self.eye_color,
            "birth_year":self.birth_year,
            "gender":self.gender,
            "homeworld_id":self.homeworld_id
        }
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_id = db.Column(db.Integer,db.ForeignKey("characters.id"))
    character = db.relationship('Characters')
    homeworld_id = db.Column(db.Integer,db.ForeignKey("planets.id"),nullable=True)
    homeworld = db.relationship('Planets')
    user_id= db.Column(db.Integer,db.ForeignKey("user.id"),nullable=True)
    user= db.relationship('User')
    
    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "homeworld_id":self.homeworld_id,
            "char_id":self.char_id
        }


