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




