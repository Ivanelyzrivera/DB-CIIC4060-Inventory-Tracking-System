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
        dbtuples = dao.getAllWarehouses()
        result =[]
        for e in dbtuples:
            result.append(self.mapToDict(e))
        return jsonify(result)