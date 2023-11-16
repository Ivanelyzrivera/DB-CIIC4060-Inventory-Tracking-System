from flask import jsonify
from dao.transactions import TransactionDAO

class TransactionHandler:

	def mapToDict(self,t):
		result = {}
		result['T_ID'] = t[0]
		result['T_Date'] = t[1]
		result['T_Quantity'] = t[2]
		result['P_ID'] = t[3]
		result['W_ID'] = t[4]
		result['U_ID'] = t[5]
		return result

	def getAllTransactions(self):
		dao = TransactionDAO()
		dbtuples = dao.getAllTransactions()
		result = []
		for e in dbtuples:
			result.append(self.mapToDict(e))
		return jsonify(result)
