from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email= db.Column(db.String(120), unique=True, nullable=False)
   
    

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
        }
class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    char_name = db.Column(db.String(50),nullable=True)
    planet_name = db.Column(db.String(250),nullable=True)
    user_id= db.Column(db.Integer,db.ForeignKey("user.id"),nullable=True)
    user= db.relationship('User')
    
    def __repr__(self):
        return self.name

    def serialize(self):
        return {
            "id":self.id,
            "user_id":self.user_id,
            "planet_name":self.planet_name,
            "char_name":self.char_name
        }


