from flask import jsonify
from dao.racks import RackDAO

class RackHandler:
    

    def mapToDict(self,t):
        result = {
            'R_ID': t[0],
            'R_Capacity': t[1],
            'R_Stock': t[2],
            'W_ID': t[3],
            'P_ID': t[4]
        }
        return result


    def getAllRacks(self):
        dao = RackDAO()
        try:
            dbtuples = dao.getAllRacks()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all racks: {e}")
            return jsonify({'error': 'An error occurred while retrieving racks'}), 500
