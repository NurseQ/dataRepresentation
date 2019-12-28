from flask import Flask, jsonify

app = Flask(__name__, static_url_path='', static_folder='.')

patient=[
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

@app.route('/patient')
def getAll():
    return jsonify(patient)

@app.route('/patient/<int:id>')
def findById(id):
    return "in find By ID for id " +str(id)

@app.route('/patient', methods = ['POST'])
def create():
    return "in create"

@app.route('/patient/<int:id>', methods=['PUT'])
def update(id):
    return "in update for id " +str(id)

@app.route('/patient/<int:id>',methods=['DELETE'])
def delete(id):
    return "in delete for id "+str(id)

if __name__ == '__main__':
    app.run(debug= True)