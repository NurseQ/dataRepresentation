from zpatientsDAO import patientsDAO

#create
latestid = patientsDAO.create(('mark', 45))

# find by id
result = patientsDAO.findByID(latestid);
print (result)

#update
patientsDAO.update(('Fred',21,latestid))
result = patientsDAO.findByID(latestid);
print (result)

# get all
allPatients = patientsDAO.getAll()
for patient in allPatients:
    print(patient)

# delete
patientsDAO.delete(latestid)