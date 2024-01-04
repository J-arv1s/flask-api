from application import db, app

app.app_context().push()

class Character(db.Model):
    __tablename__ = 'ssf2-characters'

    id = db.Column(db.Integer, primary_key=True)
    alignment = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(30), nullable=False)
    birthplace = db.Column(db.String(30), nullable=False)
    height = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, nullable=True)

    movesets = db.relationship('Moveset', backref="character", lazy=True)

    def __init__(self, alignment, name, species, birthplace, height, movesets=None, weight=None):
        self.alignment = alignment
        self.name = name
        self.species = species
        self.birthplace = birthplace
        self.height = height
        self.weight = weight

        self.movesets = movesets or []

    def __repr__(self):
        return f"Character(id: {self.id}, name: {self.name})"
    
    @property
    def json(self):
        return {
            "id": self.id,
            "alignment": self.alignment,
            "name": self.name,
            "species": self.species,
            "birthplace": self.birthplace,
            "height [cm]": self.height,
            "weight [kg]": self.weight,
            "movesets": [moveset.json for moveset in self.movesets]
        }
    
class Moveset(db.Model):
    __tablename__ = 'ssf2-characters-movesets'

    id = db.Column(db.Integer, primary_key=True)
    move_type = db.Column(db.String(100), nullable=False)
    move_name = db.Column(db.String(100), nullable=False)
    character_id = db.Column(db.Integer, db.ForeignKey('ssf2-characters.id'), nullable=False)

    @property
    def json(self):
        return {
            "id": self.id,
            "move_type": self.move_type,
            "move_name": self.move_name,
        }
