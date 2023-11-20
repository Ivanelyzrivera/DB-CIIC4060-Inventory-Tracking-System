from flask import jsonify
from dao.transactions import TransactionDAO

class TransactionHandler:

	def mapToDict(self,t):
		result = {}
		result['T_ID'] = t[0]
		result['T_Date'] = t[1]
		result['T_Year'] = t[2]
		result['T_Quantity'] = t[3]
		result['P_ID'] = t[4]
		result['W_ID'] = t[5]
		result['U_ID'] = t[6]
		return result

	def getAllTransactions(self):
		dao = TransactionDAO()
		try:
			dbtuples = dao.getAllTransactions()
			result = []
			for e in dbtuples:
				result.append(self.mapToDict(e))
			return jsonify(result)
		except Exception as e:
			print(f"An error occurred while getting all transactions: {e}")
			return jsonify({'error': 'An error occurred while retrieving transactions'}), 500

	def getTransactionByID(self, tid):
		dao = TransactionDAO()
		result = dao.getTransactionByID(tid)
		if result:
			return jsonify(self.mapToDict(result))
		else:
			return jsonify("Not found"), 404

	def insertTransaction(self, data):
		date = data['T_Date']
		year = data['T_Year']
		quantity = data['T_Quantity']
		partsID = data['P_ID']
		warehouseID = data['W_ID']
		userID = data['U_ID']
		if date and year and quantity and partsID and warehouseID and userID:
			dao = TransactionDAO()
			tid = dao.insertTransaction(date,year,quantity,partsID,warehouseID,userID)
			data['T_ID'] = tid
			return jsonify(data),201
		else:
			return jsonify("Bad Data or Unexpected attribute values, "), 400
		
		
	def putByID(self, tid, data):
		date = data['T_Date']
		year = data['T_Year']
		quantity = data['T_Quantity']
		partsID = data['P_ID']
		warehouseID = data['W_ID']
		userID = data['U_ID']
		if tid and date and year and quantity and partsID and warehouseID and userID:
			dao = TransactionDAO()
			flag = dao.putById(tid,date,year,quantity,partsID,warehouseID,userID)
			if flag:
				return jsonify(data),201
			else:
				return jsonify ("Not Found"),400
		else:
			return jsonify("Bad Data or Unexpected attribute values, "), 400
		
	def top3DaysSmallestIncoming(self, wid):
		dao = TransactionDAO()
		try:
			dbtuples = dao.top3DaysSmallestIncoming(wid)
			result = []
			for e in dbtuples:
				result.append(e)
			return jsonify(result)
		except Exception as e:
			print(f"An error occurred while getting all transactions: {e}")
			return jsonify ({'error': 'An error occurred while retrieving transactions'}), 500

	def validateUserWarehouse(self, uid, wid):
		dao = TransactionDAO()
		warehouseAssociation = dao.validateWarehouseAssociation(uid, wid)
		return warehouseAssociation is not None