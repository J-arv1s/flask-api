from application import app # app from __init__.py
from .controller import index, show, create, update, destroy

from flask import request
from werkzeug import exceptions

## COMBINING REQUEST METHODS for /characters
@app.route('/characters', methods=["GET", "POST"])
def handle_characters():
    if request.method == "GET": return index()

    if request.method == "POST": return create()

## COMBINING REQUEST METHODS for /characters/name
@app.route('/characters/<string:name>', methods=['GET'])
def handle_character(name):
    if request.method == "GET": return show(name)

## COMBINING REQUEST METHODS for /characters/id
@app.route('/characters/<int:id>', methods=['PATCH', 'DELETE'])
def handle_character_ID(id):
    if request.method == 'PATCH': return update(id)
    
    if request.method == 'DELETE': return destroy(id)



## CUSTOM ERROR HANDLERS
@app.errorhandler(exceptions.NotFound)
def handle_404(error):
    return { 'error': f'Oops {error}'}

@app.errorhandler(exceptions.InternalServerError)
def handle_500(error):
    return { 'error': f'Oops {error}'}

@app.errorhandler(exceptions.BadRequest)
def handle_400(error):
    return { 'error': f'Oops {error}'}
