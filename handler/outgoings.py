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

	def getoutgoingbyID(self , oid):
		dao = OutgoingDAO()
		result = dao.getoutgoingbyID(oid)
		if result :
			return jsonify(self.mapToDict(result))
		else:
			return jsonify("Not found"), 404
		
	def insertOutgoing(self,data):
		sellprice = data['O_SellPrice']
		customer = data['O_Customer']
		destination = data['O_Destination']
		transactionID = data['T_ID']
		if sellprice and customer and destination and transactionID:
			dao = OutgoingDAO()
			oid = dao.insertOutgoing(sellprice,customer,destination,transactionID)
			data['O_ID'] = oid
			return jsonify(data),201
		else:
			return jsonify("Bad Data or Unexpected attribute values, "), 400
		
	def deleteById(self, oid):
		dao = OutgoingDAO()
		result = dao.deleteById(oid)
		if result :
			return jsonify("Delete was Succesful"),200
		else:
			return jsonify("Not found"), 404
		
	def putByID(self,oid ,data):
		sellprice = data['O_SellPrice']
		customer = data['O_Customer']
		destination = data['O_Destination']
		transactionID = data['T_ID']
		if oid and sellprice and customer and destination and transactionID:
			dao = OutgoingDAO()
			flag = dao.putByID(oid,sellprice,customer,destination,transactionID)
			if flag:
				return jsonify(data),201
			else:
				return jsonify ("Not Found"),400
		else:
			return jsonify("Bad Data or Unexpected attribute values, "), 400