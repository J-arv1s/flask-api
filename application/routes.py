from application import app # app from __init__.py
from flask import jsonify

@app.route('/')
def welcome():
    return jsonify({
        "message": "Welcome to...",
        "description": "Super Street Fighter II Characters API",
        "endpoints": [
            "GET /",
            "GET /characters",
            "GET /characters/<string:name>",
            "POST /characters/",
            "PATCH /characters/<int:id>",
            "DELETE /characters/<int:id>"
        ]
    }), 200
