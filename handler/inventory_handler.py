from flask import jsonify

class PartHandler:
    def getAllParts(self):
        return jsonify({'id' : 2, 'name' : 'tuerca', 'color' : 'blue'})

