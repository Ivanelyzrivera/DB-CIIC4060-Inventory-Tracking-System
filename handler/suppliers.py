from flask import jsonify
from dao.suppliers import SupplierDAO

class SupplierHandler:
    

    def mapToDict(self,t):
        result = {}
        result['S_ID'] = t[0]
        result['S_Name'] = t[1]
        result['S_Address'] = t[2]
        result['S_Email'] = t[3]
        result['S_PhoneNumber'] = t[4]
        result['S_City'] = t[5]
        return result



    def getAllSuppliers(self):
        dao = SupplierDAO()
        try:
            dbtuples = dao.getAllSuppliers()
            result =[]
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all suppliers: {e}")
            return jsonify({'error': 'An error occurred while retrieving suppliers'}), 500
        
    def getsupplierbyID(self , sid):
        dao = SupplierDAO()
        result = dao.getsupplierbyID(sid)
        if result :
            return jsonify(self.mapToDict(result))
        else:
            return jsonify("Not found"), 404
    
    def insertSupplier(self,data):
        name = data['S_Name']
        address = data['S_Address']
        email = data['S_Email']
        phoneNumber = data['S_PhoneNumber']
        city = data['S_City']
        if name and address and email and phoneNumber and city:
            dao = SupplierDAO()
            sid = dao.insertSupplier(name,address,email,phoneNumber,city)
            data['S_ID'] = sid
            return jsonify(data),201
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400

    def deleteById(self, sid):
        dao = SupplierDAO()
        result = dao.deleteById(sid)
        if result :
            return jsonify("Delete was Succesful"),200
        else:
            return jsonify("Not found"), 404

    def putById(self,sid ,data):
        name = data['S_Name']
        address = data['S_Address']
        email = data['S_Email']
        phoneNumber = data['S_PhoneNumber']
        city = data['S_City']
        if sid and name and address and email and phoneNumber and city:
            dao = SupplierDAO()
            flag = dao.putById(sid,name,address,email,phoneNumber,city)
            if flag:
                return jsonify(data),201
            else:
                return jsonify ("Not Found"),400
        else:
            return jsonify("Bad Data or Unexpected attribute values, "), 400
        





