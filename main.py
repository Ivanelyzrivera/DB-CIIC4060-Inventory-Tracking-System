from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
from handler.parts import PartHandler
from handler.suppliers import SupplierHandler
from handler.warehouse import WarehouseHandler
from handler.racks import RackHandler
from handler.users import UserHandler
from handler.transactions import TransactionHandler
from handler.outgoings import OutgoingHandler
from handler.incomings import IncomingHandler
from handler.exchanges import ExchangeHandler



app = Flask(__name__)

#apply Cors
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is a test file'

@app.route('/DB_Project/Allparts',methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'GET':
        return PartHandler().getAllParts()
    elif request.method == 'POST':
        data = request.json
        return PartHandler().insertPart(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/DB_Project/parts/<int:pid>')
def getpartbyID(pid):
    return PartHandler().getpartbyID(pid)



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

@app.route('/DB_Project/Alltransactions')
def getAllTransactions():
	return TransactionHandler().getAllTransactions()

@app.route('/DB_Project/Alloutgoings')
def getAllOutgoings():
	return OutgoingHandler().getAllOutgoings()

@app.route('/DB_Project/Allincomings')
def getAllIncomings():
	return IncomingHandler().getAllIncomings()

@app.route('/DB_Project/Allexchanges')
def getAllExchanges():
	return ExchangeHandler().getAllExchanges()

if __name__ == '__main__':
    app.run(debug=True)
