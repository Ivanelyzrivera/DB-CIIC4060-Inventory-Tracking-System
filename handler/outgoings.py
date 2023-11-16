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
		dbtuples = dao.getAllOutgoings()
		result = []
		for e in dbtuples:
			result.append(self.mapToDict(e))
		return jsonify(result)