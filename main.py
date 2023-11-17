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

@app.route('/parts',methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'GET':
        return PartHandler().getAllParts()
    elif request.method == 'POST':
        data = request.json
        return PartHandler().insertPart(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/parts/<int:pid>',methods = ['GET','PUT','DELETE'])
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
    
@app.route('/parts/price/<int:pid>', methods = ['GET'])
def getpricebyID(pid):
     return PartHandler().getpricebyID(pid)

@app.route('/parts/allprice', methods = ['GET'])
def getAllPriceOfParts():
     return PartHandler().getAllPriceOfParts()

@app.route('/parts/supplier/<int:sid>', methods = ['GET'])
def partsSupliedBySupplier(sid):
     return PartHandler().partsSupliedBySupplier(sid)

@app.route('/parts/rack/<int:rid>',methods = ['GET'])
def partsInRack(rid):
     return PartHandler().partsInRack(rid)

     

@app.route('/suppliers', methods = ['GET','POST'])
def getAllSuppliers():
    if request.method == 'GET':
        return SupplierHandler().getAllSuppliers()
    elif request.method == 'POST':
        data = request.json
        return SupplierHandler().insertSupplier(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/suppliers/<int:sid>',methods = ['GET','PUT','DELETE'])
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


@app.route('/warehouses',methods=['GET', 'POST']) # return WarehouseHandler().getAllWarehouses()
def getAllWarehouses():
    if request.method == 'GET':
        return  WarehouseHandler().getAllWarehouses()
    elif request.method == 'POST':
        data = request.json
        return WarehouseHandler().insertWarehouse(data)
    else:
        return jsonify("NOT SUPPORTED"),405
    

@app.route('/warehouses/<int:wid>',methods = ['GET','PUT','DELETE'])
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
#started route and logic for lowstock
# @app.route('warehouse/<int:wid>/rack/lowstock')
# def getlowstockracks(wid):
#      racks = []
#      for rack in RackHandler().getAllRacks():
#           if 
          
#@app.route('/DB_Project/Allracks')
#def getAllRacks():
#    return RackHandler().getAllRacks()


@app.route('/racks',methods=['GET', 'POST'])
def getAllRacks():
    if request.method == 'GET':
        return RackHandler().getAllRacks()
    elif request.method == 'POST':
        data = request.json
        return RackHandler().insertRacks(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/racks/<int:rid>',methods = ['GET','PUT','DELETE'])
def getracksbyID(rid):
    if request.method == 'GET':
         return RackHandler().getracksID(rid)
    elif request.method == 'DELETE':
         return RackHandler().deleteById(rid)
    elif request.method == 'PUT':
         data = request.json
         return RackHandler().putById(rid,data)
    else:
         return jsonify("NOT SUPPORTED"),405
    
@app.route('/racks/quantity/<int:rid>', methods = ['GET'])
def quantityOfPartsInRack(rid):
    return RackHandler().quantityOfPartsInRack(rid)



@app.route('/users',methods=['GET', 'POST'])
def getAllUsers():
    if request.method == 'GET':
        return UserHandler().getAllUsers()
    elif request.method == 'POST':
        data = request.json
        return UserHandler().insertUser(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/users/<int:uid>',methods = ['GET','PUT','DELETE'])
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
    


@app.route('/transactions',methods=['GET', 'POST'])
def getAllTransactions():
    if request.method == 'GET':
        return TransactionHandler().getAllTransactions()
    elif request.method == 'POST':
        data = request.json
        return TransactionHandler().insertTransaction(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/transactions/<int:tid>',methods = ['GET','PUT'])
def getTransactionByID(tid):
    if request.method == 'GET':
         return TransactionHandler().getTransactionByID(tid)
    elif request.method == 'PUT':
         data = request.json
         return TransactionHandler().putById(tid,data)
    else:
         return jsonify("NOT SUPPORTED"),405



@app.route('/outgoings',methods=['GET', 'POST'])
def getAllOutgoings():
    if request.method == 'GET':
        return OutgoingHandler().getAllOutgoings()
    elif request.method == 'POST':
        data = request.json
        return OutgoingHandler().insertOutgoing(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/outgoings/<int:oid>',methods = ['GET','PUT','DELETE'])
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

@app.route('/incomings',methods=['GET', 'POST'])
def getAllIncomings():
    if request.method == 'GET':
        return IncomingHandler().getAllIncomings()
    elif request.method == 'POST':
        data = request.json
        return IncomingHandler().insertIncoming(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/incomings/<int:iid>',methods = ['GET','PUT','DELETE'])
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
# @app.route('/DB_Project/Allincomings')
# def getAllIncomings():
# 	return IncomingHandler().getAllIncomings()

@app.route('/exchanges',methods=['GET', 'POST'])
def getAllExchanges():
    if request.method == 'GET':
        return ExchangeHandler().getAllExchanges()
    elif request.method == 'POST':
        data = request.json
        return ExchangeHandler().insertExchange(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/exchanges/<int:eid>',methods = ['GET','PUT','DELETE'])
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
# @app.route('/DB_Project/Allexchanges')
# def getAllExchanges():
# 	return ExchangeHandler().getAllExchanges()


# STATISTIC
@app.route('/most/rack', methods = ['GET'])
def getTop10WarehousesMostRacks():
     return WarehouseHandler().getTop10WarehousesMostRacks()

if __name__ == '__main__':
    app.run(debug=True)
