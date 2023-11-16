from flask import jsonify
from dao.parts import PartDAO

class PartHandler:
    

    def mapToDict(self,t):
        result = {}
        dict['P_ID'] = t[0]
        dict['P_Type'] = t[1]
        dict['P_Color'] = t[2]
        dict['P_Weight'] = t[3]
        dict['P_Name'] = t[4]
        dict['P_Price'] = t[5]
        dict['P_Manufacturer'] = t[6]
        dict['S_ID'] = t[7]
        return result



    def getAllParts(self):
        dao = PartDAO()
        dbtuples = dao.getAllParts()
        result =[]
        for e in dbtuples:
            result.append(self.mapToDict(e))
        return jsonify(result)




