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

@app.route('/datavengers/parts',methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'GET':
        return PartHandler().getAllParts()
    elif request.method == 'POST':
        data = request.json
        return PartHandler().insertPart(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/parts/<int:pid>',methods = ['GET','PUT','DELETE'])
def getpartbyID(pid):
    if request.method == 'GET':
         return PartHandler().getpartbyID(pid)
    elif request.method == 'DELETE':
         return PartHandler().deleteById(pid)
    elif request.method == 'PUT':
         data = request.json
         return PartHandler().putById(pid,data)
    else:
         return jsonify("NOT SUPPORTED"),405
    
@app.route('/datavengers/parts/price/<int:pid>', methods = ['GET'])
def getpricebyID(pid):
     return PartHandler().getpricebyID(pid)

@app.route('/datavengers/parts/allprice', methods = ['GET'])
def getAllPriceOfParts():
     return PartHandler().getAllPriceOfParts()

@app.route('/datavengers/parts/supplier/<int:sid>', methods = ['GET'])
def partsSupliedBySupplier(sid):
     return PartHandler().partsSupliedBySupplier(sid)

@app.route('/datavengers/parts/rack/<int:rid>',methods = ['GET'])
def partsInRack(rid):
     return PartHandler().partsInRack(rid)

     

@app.route('/datavengers/suppliers', methods = ['GET','POST'])
def getAllSuppliers():
    if request.method == 'GET':
        return SupplierHandler().getAllSuppliers()
    elif request.method == 'POST':
        data = request.json
        return SupplierHandler().insertSupplier(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/suppliers/<int:sid>',methods = ['GET','PUT','DELETE'])
def getsupplierbyID(sid):
    if request.method == 'GET':
         return SupplierHandler().getsupplierbyID(sid)
    elif request.method == 'DELETE':
         return SupplierHandler().deleteById(sid)
    elif request.method == 'PUT':
         data = request.json
         return SupplierHandler().putById(sid,data)
    else:
         return jsonify("NOT SUPPORTED"),405


@app.route('/datavengers/warehouses',methods=['GET', 'POST']) # return WarehouseHandler().getAllWarehouses()
def getAllWarehouses():
    if request.method == 'GET':
        return  WarehouseHandler().getAllWarehouses()
    elif request.method == 'POST':
        data = request.json
        return WarehouseHandler().insertWarehouse(data)
    else:
        return jsonify("NOT SUPPORTED"),405
    

@app.route('/datavengers/warehouses/<int:wid>',methods = ['GET','PUT','DELETE'])
def getwarehousebyID(wid):
    if request.method == 'GET':
         return WarehouseHandler().getwarehousebyID(wid)
    elif request.method == 'DELETE':
         return WarehouseHandler().deleteById(wid)
    elif request.method == 'PUT':
         data = request.json
         return WarehouseHandler().putById(wid,data)
    else:
         return jsonify("NOT SUPPORTED"),405


@app.route('/datavengers/racks',methods=['GET', 'POST'])
def getAllRacks():
    if request.method == 'GET':
        return RackHandler().getAllRacks()
    elif request.method == 'POST':
        data = request.json
        return RackHandler().insertRack(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/racks/<int:rid>',methods = ['GET','PUT','DELETE'])
def getracksbyID(rid):
    if request.method == 'GET':
         return RackHandler().getracksbyID(rid)
    elif request.method == 'DELETE':
         return RackHandler().deleteById(rid)
    elif request.method == 'PUT':
         data = request.json
         return RackHandler().putById(rid,data)
    else:
         return jsonify("NOT SUPPORTED"),405


@app.route('/datavengers/users',methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'GET':
        return UserHandler().getAllUsers()
    elif request.method == 'POST':
        data = request.json
        return UserHandler().insertUser(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/users/<int:uid>',methods = ['GET','PUT','DELETE'])
def getuserbyID(uid):
    if request.method == 'GET':
         return UserHandler().getuserbyID(uid)
    elif request.method == 'DELETE':
         return UserHandler().deleteById(uid)
    elif request.method == 'PUT':
         data = request.json
         return UserHandler().putById(uid,data)
    else:
         return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/transactions',methods=['GET', 'POST'])
def getAllTransactions():
    if request.method == 'GET':
        return TransactionHandler().getAllTransactions()
    elif request.method == 'POST':
        data = request.json
        return TransactionHandler().insertTransaction(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/transactions/<int:tid>',methods = ['GET','PUT'])
def getTransactionByID(tid):
    if request.method == 'GET':
         return TransactionHandler().getTransactionByID(tid)
    elif request.method == 'PUT':
         data = request.json
         return TransactionHandler().putById(tid,data)
    else:
         return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/outgoings',methods=['GET', 'POST'])
def getAllOutgoings():
    if request.method == 'GET':
        return OutgoingHandler().getAllOutgoings()
    elif request.method == 'POST':
        data = request.json
        return OutgoingHandler().insertOutgoing(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/outgoings/<int:oid>',methods = ['GET','PUT','DELETE'])
def getoutgoingbyID(oid):
    if request.method == 'GET':
         return OutgoingHandler().getoutgoingbyID(oid)
    elif request.method == 'DELETE':
         return OutgoingHandler().deleteById(oid)
    elif request.method == 'PUT':
         data = request.json
         return OutgoingHandler().putById(oid,data)
    else:
         return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/incomings',methods=['GET', 'POST'])
def getAllIncomings():
    if request.method == 'GET':
        return IncomingHandler().getAllIncomings()
    elif request.method == 'POST':
        data = request.json
        return IncomingHandler().insertIncoming(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/incomings/<int:iid>',methods = ['GET','PUT','DELETE'])
def getincomingbyID(iid):
    if request.method == 'GET':
         return IncomingHandler().getincomingbyID(iid)
    elif request.method == 'DELETE':
         return IncomingHandler().deleteById(iid)
    elif request.method == 'PUT':
         data = request.json
         return IncomingHandler().putById(iid,data)
    else:
         return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/exchanges',methods=['GET', 'POST'])
def getAllExchanges():
    if request.method == 'GET':
        return ExchangeHandler().getAllExchanges()
    elif request.method == 'POST':
        data = request.json
        return ExchangeHandler().insertExchange(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/datavengers/exchanges/<int:eid>',methods = ['GET','PUT','DELETE'])
def getexchangebyID(eid):
    if request.method == 'GET':
         return ExchangeHandler().getexchangebyID(eid)
    elif request.method == 'DELETE':
         return ExchangeHandler().deleteById(eid)
    elif request.method == 'PUT':
         data = request.json
         return ExchangeHandler().putById(eid,data)
    else:
         return jsonify("NOT SUPPORTED"),405

# GLOBAL STATISTICS
@app.route('/datavengers/most/rack', methods = ['GET'])
def getTop10WarehousesMostRacks():
     return WarehouseHandler().getTop10WarehousesMostRacks()

@app.route('/datavengers/most/incoming', methods = ['GET'])
def getTop5WarehousesMostIncomings():
     return WarehouseHandler().getTop5WarehousesMostIncomings()

@app.route('/datavengers/most/deliver', methods = ['GET'])
def getTop5WarehousesThatDeliverMostExchanges():
     return WarehouseHandler().getTop5WarehousesThatDeliverMostExchanges()

@app.route('/datavengers/most/transactions', methods = ['GET'])
def getTop3UsersMostTransactions():
    return UserHandler().getTop3UsersMostTransactions()

@app.route('/datavengers/most/transaction', methods = ['GET'])
def getTop3WarehousesLeastOutgoings(self):
    return WarehouseHandler().getTop3WarehousesLeastOutgoings()

@app.route('/datavengers/most/city', methods = ['GET'])
def getTop3WarehouseCitiesMostTransactions():
    return WarehouseHandler().getTop3WarehouseCitiesMostTransactions()

if __name__ == '__main__':
    app.run(debug=True)
