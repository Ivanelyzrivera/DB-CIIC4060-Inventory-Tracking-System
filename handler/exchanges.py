from flask import jsonify
from dao.exchanges import ExchangeDAO

class ExchangeHandler:
    

    def mapToDict(self,t):
        result = {
            'E_ID': t[0],
            'E_Reason': t[1],
            'W_ID_Destination': t[2],
            'U_ID_Destination': t[3],
            'T_ID': t[4]
        }
        return result


    def getAllExchanges(self):
        dao = ExchangeDAO()
        # try:
        dbtuples = dao.getAllExchanges()
        result = []
        for e in dbtuples:
            result.append(self.mapToDict(e))
        return jsonify(result)
        # except Exception as e:
        #     print(f"An error occurred while getting all exchanges: {e}")
        #     return jsonify({'error': 'An error occurred while retrieving exchanges'}), 500
