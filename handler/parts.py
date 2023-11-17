from flask import jsonify
from dao.parts import PartDAO

class PartHandler:
    

    def mapToDict(self,t):
        result = {}
        result['P_ID'] = t[0]
        result['P_Type'] = t[1]
        result['P_Color'] = t[2]
        result['P_Weight'] = t[3]
        result['P_Name'] = t[4]
        result['P_Price'] = t[5]
        result['P_Manufacturer'] = t[6]
        result['S_ID'] = t[7]
        return result


    def getAllParts(self):
        dao = PartDAO()
        try:
            dbtuples = dao.getAllParts()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all parts: {e}")
            return jsonify({'error': 'An error occurred while retrieving parts'}), 500

    def getpartbyID(self , pid):
        dao = PartDAO()
        result = dao.getpartbyID(pid)
        if result :
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not found"), 404

    def insertPart(self,data):
        type = data['P_Type']
        color = data['P_Color']
        weight = data['P_Weight']
        name = data['P_Name']
        price = data['P_Price']
        manufacturer = data['P_Manufacturer']
        supplierID = data['S_ID']
        if type and color and weight and name and price and manufacturer and supplierID:
            dao = PartDAO()
            pid = dao.insertPart(type,color,weight,name,price,manufacturer,supplierID)
            data['P_ID'] = pid
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        

    def deleteById(self, pid):
        dao = PartDAO()
        result = dao.deleteById(pid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404

    def putById(self,pid ,data):
        type = data['P_Type']
        color = data['P_Color']
        weight = data['P_Weight']
        name = data['P_Name']
        price = data['P_Price']
        manufacturer = data['P_Manufacturer']
        supplierID = data['S_ID']
        if pid and type and color and weight and name and price and manufacturer and supplierID:
            dao = PartDAO()
            flag = dao.putById(pid,type,color,weight,name,price,manufacturer,supplierID)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        

    def getpricebyID(self , pid):
        dao = PartDAO()
        result = dao.getpartbyID(pid)
        if result :
            return jsonify(result[5],)
        else:
            return jsonify("Not found"), 404
        

    def getAllPriceOfParts(self):
        dao = PartDAO()
        try:
            part_prices = dao.getAllPriceOfParts()
            return jsonify(part_prices)
        except Exception as e:
            return jsonify({'error': 'An error occurred while retrieving part prices'}), 500

        

