from flask import jsonify, request
from werkzeug import exceptions
from .models import Character

from .. import db

def index():
    characters = Character.query.order_by(Character.id).all()
    try:
        return jsonify({ "ssf2-fighters": [c.json for c in characters] }), 200
    except:
        raise exceptions.InternalServerError(f"Work-in-Progress")
    
def show(name):
    print('name', type(name))
    character = Character.query.filter_by(name=name).first()

    try:
        return jsonify({f'ssf2-fighter[{name}]': character.json}), 200
    except:
        raise exceptions.NotFound(f"Character name not found in DB")
    
def create():
    try:
        alignment, name, species, birthplace, height, movesets, weight = request.json.values()

        new_character = Character(alignment, name, species, birthplace, height, weight, movesets)

        db.session.add(new_character)
        db.session.commit()

        return jsonify({ "new ssf2-fighter": new_character.json }), 201
    except:
        raise exceptions.BadRequest(f"Cannot process request")

def update(id):
    data = request.json
    character = Character.query.filter_by(id=id).first()
    char_name = character.name
    for attribute, value in data.items():
        if hasattr(character, attribute):
            setattr(character, attribute, value)
    
    db.session.commit()
    return jsonify({ f'updating ssf2-fighter[{char_name}]': character.json})

def destroy(id):
    character = Character.query.filter_by(id=id).first()
    db.session.delete(character)
    db.session.commit()
    return 'Character deleted', 204
