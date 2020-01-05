from flask import Flask, jsonify, request, abort
from zpatientsDAO import patientDAO

app = Flask(__name__, static_url_path='', static_folder='.')


# @app.route('/')
# def index():
#     return 'Hello, World!'

@app.route('/patients')
def getAll():
    results = patientDAO.getAll()
    return jsonify(results)

@app.route('/patients/<int:id>')
def findById(id):
    foundPatient = patientDAO.findByID(id)
    return jsonify(foundPatient)

# curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Jay Leno\", \"Diagnosis\":\"STI\",\"DOB\":\"1950/07/15\",\"Doctor\":\"Dr. Zimmer\",\"Gender\":\"Male\"}" http://127.0.0.1:5000/patients
@app.route('/patients', methods = ['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking
    patient = {
        
        "Name": request.json['Name'],
        "Diagnosis": request.json['Diagnosis'],
        "DOB": request.json['DOB'],
        "Doctor": request.json['Doctor'],
        "Gender": request.json['Gender'],
    }
    values = (patient['Name'], patient['Diagnosis'], patient['DOB'], patient['Doctor'], patient['Gender']) 
    newId = patientDAO.create(values)
    patient['id'] = newId
        
    return jsonify(patient)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Jay Leno\", \"Diagnosis\":\"STI\",\"DOB\":\"1950/07/15\",\"Doctor\":\"Dr. Zimmer\",\"Gender\":\"Male\"}" http://127.0.0.1:5000/patients/1
@app.route('/patients/<int:id>', methods=['PUT'])
def update(id):
    foundPatient =  patientDAO.findByID(id)
    if not foundPatient:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Name' in reqJson:
        foundPatient['Name'] = reqJson['Name']
    if 'Diagnosis' in reqJson:
        foundPatient['Diagnosis'] = reqJson['Diagnosis']
    if 'DOB' in reqJson:
        foundPatient['DOB'] = reqJson['DOB']
    if 'Doctor' in reqJson:
        foundPatient['Doctor'] = reqJson['Doctor']
    if 'Gender' in reqJson:
        foundPatient['Gender'] = reqJson['Gender']
    values = (foundPatient['Name'], foundPatient['Diagnosis'], foundPatient['DOB'], foundPatient['Doctor'], foundPatient['Gender'], foundPatient['id'])
    patientDAO.update(values)

    return jsonify(foundPatient)

@app.route('/patients/<int:id>',methods=['DELETE'])
def delete(id):
    patientDAO.delete(id)
    return jsonify({"done":True})

if __name__ == '__main__':
    app.run(debug= True)