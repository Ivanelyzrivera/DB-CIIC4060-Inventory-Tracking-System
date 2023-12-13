from flask import jsonify
from dao.outgoings import OutgoingDAO
from dao.transactions import TransactionDAO
from dao.parts import PartDAO
from dao.racks import RackDAO

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
		date = data['T_Date']
		year = data['T_Year']
		quantity = data['T_Quantity']
		partID = data['P_ID']
		warehouseID = data['W_ID']
		userID = data['U_ID']

		dao = OutgoingDAO()

		warehouseStockRes = PartDAO().getPartStockInWarehouse(warehouseID,partID)
		warehouseStock = 0
		for e in warehouseStockRes:
			warehouseStock = e[1]
			break

		if quantity > warehouseStock:
			return jsonify("Bad Data or Unexpected attribute values (Requested quantity larger than warehouse stock), "), 400

		transactionID = TransactionDAO().insertTransaction(date,year,quantity,partID,warehouseID,userID)

		foundRackRemove = dao.findRackToPlace(partID, warehouseID)
		quantityToRemove = quantity

		if transactionID:

			for e in foundRackRemove:
				rackID = e[2]
				rackStock = e[3]
				rackCapacity = e[4]
				if quantityToRemove >= rackStock:
					quantityToRemove -= rackStock
					rackStock = 0
					emptiedRack = RackDAO().putByID(rackID,rackCapacity,rackStock,warehouseID,partID)
				else:
					rackStock -= quantityToRemove
					quantityToRemove = 0
					updatedRack = RackDAO().putByID(rackID,rackCapacity,rackStock,warehouseID,partID)
				
            
			sellprice = data['O_SellPrice']
			customer = data['O_Customer']
			destination = data['O_Destination']
			if sellprice and customer and destination and transactionID:
				oid = dao.insertOutgoing(sellprice,customer,destination,transactionID)
				data['O_ID'] = oid
				data['T_ID'] = transactionID
				return jsonify(data),201
			else:
				return jsonify("Bad Data or Unexpected attribute values, "), 400
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