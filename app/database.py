from . import db

class Pokemon(db.Model):
    __tablename__ = "pokemon"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    type1 = db.Column(db.String, nullable=False)
    type2 = db.Column(db.String)
    generation = db.Column(db.Integer, nullable=False)
    dexnumber = db.Column(db.Integer, nullable=False)
