from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
from handler.parts import PartHandler
from handler.suppliers import SupplierHandler
from handler.warehouse import WarehouseHandler
from handler.racks import RackHandler
from handler.transactions import TransactionHandler
from handler.users import UserHandler


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

@app.route('/DB_Project/Allwarehouses')
def getAllWarehouses():
    return WarehouseHandler().getAllWarehouses()

@app.route('/DB_Project/Allracks')
def getAllRacks():
    return RackHandler().getAllRacks()

@app.route('/DB_Project/Allusers')
def getAllUsers():
    return UserHandler().getAllUsers()



if __name__ == '__main__':
    app.run(debug=True)
