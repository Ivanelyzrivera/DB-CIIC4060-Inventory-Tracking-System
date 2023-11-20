from flask import jsonify
from dao.warehouse import WarehouseDAO

class WarehouseHandler:
    
    def mapToDict(self,t):
        result = {}
        result['W_ID'] = t[0]
        result['W_Name'] = t[1]
        result['W_Address'] = t[2]
        result['W_City'] = t[3]
        return result


    def getAllWarehouses(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.getAllWarehouses()
            result =[]
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500


    def getwarehousebyID(self , wid):
        dao = WarehouseDAO()
        result = dao.getwarehousebyID(wid)
        if result :
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not found"), 404
        
    
    def insertWarehouse(self,data):
        name = data['W_Name']
        address = data['W_Address']
        city = data['W_City']
        if  name and address and city:
            dao = WarehouseDAO()
            wid = dao.insertWarehouse(name,address,city)
            data['W_ID'] = wid
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        

    def deleteById(self, wid):
        dao = WarehouseDAO()
        result = dao.deleteById(wid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404

    def putById(self,wid ,data):
        name = data['W_Name']
        address = data['W_Address']
        city = data['W_City']
        if wid and name and address and city:
            dao = WarehouseDAO()
            flag = dao.putById(wid, name,address,city)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        
    def getTop10WarehousesMostRacks(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.getTop10WarehousesMostRacks()
            result =[]
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500
        
    def getTop5WarehousesMostIncomings(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.getTop5WarehousesMostIncomings()
            result =[]
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500
        
    def getTop5WarehousesThatDeliverMostExchanges(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.getTop5WarehousesThatDeliverMostExchanges()
            result =[]
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500

    def getTop3WarehouseCitiesMostTransactions(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.getTop3WarehouseCitiesMostTransactions()
            result =[]
            for e in dbtuples:
                result.append(e)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500   

    def getTop3WarehousesLeastOutgoings(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.getTop3WarehousesLeastOutgoings()
            result = []
            for e in dbtuples:
                result.append(e)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500
        
   
    def getProfitByYear(self, wid):
        dao = WarehouseDAO()
        dbtuples = dao.getProfitByYear(wid)
    

        if dbtuples:
            result = []
            for row in dbtuples:
                result.append({
                    'profit_year': row[0],
                    'profit': row[1]
                })
            print(result)
            return jsonify(result)
        else:
            return jsonify("Not found"), 404








         
    def partTypeByWarehouse(self):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.partTypeByWarehouse()
            result =[]
            for e in dbtuples:
                result.append(e)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving warehouses'}), 500
        

    def warehouseRackLowStock(self, wid): # Top 5 racks with quantity under the 25% capacity
        dao = WarehouseDAO()
        try:
            dbtuples = dao.warehouseRackLowStock(wid)
            result = []
            for e in dbtuples:
                rack_info = {
                    'RackID': e[0],
                    'Capacity': e[1],
                    'Stock': e[2],
                    'WarehouseID': e[3],
                    'PartID': e[4]
                }
                result.append(rack_info)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting the low stock racks: {e}")
            return jsonify({'error': 'An error occurred while retrieving low stock racks'}), 400
        
        
    def warehouseBottom3(self, wid):
        dao = WarehouseDAO()
        try:
            dbtuples = dao.warehouseBottom3(wid)
            result =[]
            for e in dbtuples:
                result.append(e)
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting bottom 3 type/material from the warehouses: {e}")
            return jsonify({'error': 'An error occurred while retrieving  bottom 3 type/material'}), 500

    def validateUserWarehouse(self, uid, wid):
        dao = WarehouseDAO()
        warehouseAssociation = dao.validateWarehouseAssociation(uid, wid)
        return warehouseAssociation is not None