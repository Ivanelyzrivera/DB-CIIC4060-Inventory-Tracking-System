from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
from handler.parts import PartHandler
from handler.suppliers import SupplierHandler


app = Flask(__name__)

#apply Cors
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is a test file'

@app.route('/DB_Project/Allparts')
def getAllParts():
    return PartHandler().getAllParts()

@app.route('/DB_Project/Allsuppliers')
def getAllSuppliers():
    return SupplierHandler().getAllSuppliers()


if __name__ == '__main__':
    app.run(debug=True)
