from flask import Blueprint, jsonify
from .database import Pokemon
from . import db
import random

api = Blueprint("api", __name__)

@api.route("/random-pokemon", methods=["GET"])
def get_random_pokemon():
    # Abfrage eines zufälligen Pokémon
    pokemon = db.session.execute(db.select(Pokemon).order_by(db.func.random())).scalar()
    
    if pokemon:
        return jsonify({
            "id": pokemon.id,
            "name": pokemon.name,
            "type1": pokemon.type1,
            "type2": pokemon.type2,
            "generation": pokemon.generation,
            "dexnumber": pokemon.dexnumber
        })
    else:
        return jsonify({"error": "No Pokémon found"}), 404
