from flask import jsonify
from dao.parts import PartDAO

class PartHandler:
    

    def mapToDict(self,t):
        result = {}
        result['P_ID'] = t[0]
        result['P_Type'] = t[1]
        result['P_Color'] = t[2]
        result['P_Weight'] = t[3]
        result['P_Name'] = t[4]
        result['P_Price'] = t[5]
        result['P_Manufacturer'] = t[6]
        result['S_ID'] = t[7]
        return result



    # def getAllParts(self):
    #     dao = PartDAO()
    #     dbtuples = dao.getAllParts()
    #     result =[]
    #     for e in dbtuples:
    #         result.append(self.mapToDict(e))
    #     return jsonify(result)

    def getAllParts(self):
        dao = PartDAO()
        try:
            dbtuples = dao.getAllParts()
            result = []
            for e in dbtuples:
                result.append(self.mapToDict(e))
            return jsonify(result)
        except Exception as e:
            print(f"An error occurred while getting all parts: {e}")
            return jsonify({'error': 'An error occurred while retrieving parts'}), 500
