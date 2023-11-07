from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
from handler import inventory_handler

app = Flask(__name__)

#apply Cors
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is a test file asdasd'

@app.route('/DB_Project/getAllparts')
def getAllParts():
    return PartHandler().getAllParts()

if __name__ == '__main__':
    app.run(debug=True)
