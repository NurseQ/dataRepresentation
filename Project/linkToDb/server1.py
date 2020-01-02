from flask import Flask, jsonify, request, abort
from zpatientsDAO import patientsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

patients=[
    {"id":1, "Name":"James Bond", "Diagnosis": "Myocardial Infarc", "DOB": "1960/01/28", "Doctor": "Dr. Murphy", "Gender": "Male"},
    {"id":2, "Name":"John Doe", "Diagnosis": "Gastric Ulcer", "DOB": "1970/09/02", "Doctor": "Dr. O'Shea", "Gender": "Male"},
    {"id":3, "Name":"Joyce James", "Diagnosis": "Dementia", "DOB": "1940/11/15", "Doctor": "Dr. Green", "Gender": "Female"},
    {"id":4, "Name":"Liz Hurling", "Diagnosis": "Arthritis", "DOB": "1975/12/07", "Doctor": "Dr. Who", "Gender": "Female"},
    {"id":5, "Name":"Lance Strongarm", "Diagnosis": "Alcohol Poisoning", "DOB": "2002/02/29", "Doctor": "Dr. Murphy", "Gender": "Male"}
]

nextId=6

# @app.route('/')
# def index():
#     return 'Hello, World!'

@app.route('/patients')
def getAll():
    results = patientsDAO.getAll()
    return jsonify(results)

@app.route('/patients/<int:id>')
def findById(id):
    foundPatient = patientsDAO.findByID(id)
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
     
    patients.append(patient)
    return jsonify(patient)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Jay Leno\", \"Diagnosis\":\"STI\",\"DOB\":\"1950/07/15\",\"Doctor\":\"Dr. Zimmer\",\"Gender\":\"Male\"}" http://127.0.0.1:5000/patients/1
@app.route('/patients/<int:id>', methods=['PUT'])
def update(id):
    foundPatients =  list(filter(lambda b: b['id']==id, patients))
    if len(foundPatients) ==0:
        abort(404)
    foundPatient = foundPatients[0]
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
    return jsonify(foundPatient)

@app.route('/patients/<int:id>',methods=['DELETE'])
def delete(id):
    foundPatients =  list(filter(lambda b: b['id']==id, patients))
    if len(foundPatients) ==0:
        abort(404)
    patients.remove(foundPatients[0])
    return jsonify({"done":True})

if __name__ == '__main__':
    app.run(debug= True)