from flask import jsonify
from dao.outgoings import OutgoingDAO

class OutgoingHandler:

	def mapToDict(self,t):
		result = {
		'O_ID' : t[0],
		'O_SellPrice' : t[1],
		'O_Customer' : t[2],
		'O_Destination' : t[3],
		'T_ID' : t[4]
		}
		return result

	def getAllOutgoings(self):
		dao = OutgoingDAO()
		try:
			dbtuples = dao.getAllOutgoings()
			result = []
			for e in dbtuples:
				result.append(self.mapToDict(e))
			return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all outgoings: {e}")
            return jsonify({'error': 'An error occurred while retrieving outgoings'}), 500
