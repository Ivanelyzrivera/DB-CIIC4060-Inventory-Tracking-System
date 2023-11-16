from flask import jsonify
from dao.incomings import IncomingDAO

class IncomingHandler:
    

    def mapToDict(self,t):
        result = {
            'I_ID': t[0],
            'R_Capacity': t[1],
            'S_Stock': t[2],
            'T_ID': t[3]
        }
        return result


    def getAllIncomings(self):
        dao = IncomingDAO()
        try:
            dbtuples = dao.getAllIncomings()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all incomings: {e}")
            return jsonify({'error': 'An error occurred while retrieving incomings'}), 500
