from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
from handler.parts import PartHandler
from handler.suppliers import SupplierHandler


app = Flask(__name__)

#apply Cors
CORS(app)

@app.route('/')
def greeting():
    return 'Hello, this is a test file'

@app.route('/DB_Project/Allparts',methods=['GET', 'POST'])
def getAllParts():
    if request.method == 'GET':
        return PartHandler().getAllParts()
    elif request.method == 'POST':
        data = request.json
        return PartHandler().insertPart(data)
    else:
        return jsonify("NOT SUPPORTED"),405

@app.route('/DB_Project/parts/<int:pid>')
def getpartbyID(pid):
    return PartHandler().getpartbyID(pid)



@app.route('/DB_Project/Allsuppliers')
def getAllSuppliers():
    return SupplierHandler().getAllSuppliers()


if __name__ == '__main__':
    app.run(debug=True)
