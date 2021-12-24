import json
import inspect
from re import I, U
import sys, os
import random
from marshmallow.utils import pprint
import requests

# add app path 
sys.path.append(os.path.abspath(os.path.join('../../..')))

from api.src.models.laborder import TestType
import api.src.repositories.patient as patient
import api.src.repositories.physician as physician
import api.src.repositories.laborder as laborder
import api.src.models.schema as schema

from api import db

p = patient.PatientRepo()
md = physician.PhysicianRepo()
lo = laborder.LabOrderRepo()

patient_url = "http://127.0.0.1:5000/records/"
physician_url = "http://127.0.0.1:5000/physicians/"
laborder_url = "http://127.0.0.1:5000/laborder/"
mock_data = "api/src/utils/mock_data/"

# retrieve TestType enum attributes and put them into a list
attributes = inspect.getmembers(TestType, lambda a:not(inspect.isroutine(a)))
test_types = [a[0] for a in attributes if not(a[0].startswith('__') and a[0].endswith('__'))] # we get more than just test types
tests = test_types[0:15] # take only actual test types 
tests_len = len(tests) - 1

# load all mock data
with open(mock_data + 'patients.json') as patients:
    patient_data = json.load(patients)

with open(mock_data + 'physicians.json') as physicians:
    physician_data = json.load(physicians)

with open(mock_data+ 'lab_orders.json') as labs:
    labs_data = json.load(labs)


pcp_ids = []
pcp_id = 1 # assume first md will be assigned id of 1. Rewrite later to be more elegant
for dr in physician_data:
    pcp_ids.append(pcp_id)
    pcp_id += 1
    s = schema.PhysicianSchema()
    result = s.load(dr)
    doc = md.create(**result)
    doc.save() 
    print("Added Dr.", dr["last_name"], "to the physician table!\n")
    
patient_ids = []
patient_id = 1 # assume first patient will be assigned id of 1. Rewrite as stated above
for patient in patient_data:
    patient["pcp_id"] = pcp_ids[random.randrange(0,len(pcp_ids))]
    print(patient['first_name'], patient["pcp_id"])
    patient["medications"] = ""
    patient_ids.append(patient_id)
    patient_id += 1
    s = schema.PatientSchema()
    result = s.load(patient)
    print(result)
    patientmodel = p.create(**result)
    patientmodel.save()
    print("Added patient:", patient["first_name"], patient["last_name"], "to the patient table!\n")

laborder_id = 1 # assume first lab order is 1. Rewrite "
for lab in labs_data:
    lab["test_type"] = tests[random.randrange(0,tests_len)]
    lab["physician_id"] = pcp_ids[random.randrange(0,len(pcp_ids)-1)]
    lab["patient_id"] = patient_ids[random.randrange(0,len(patient_ids)-1)]
    s = schema.LabOrderSchema()
    result = s.load(lab)
    order = lo.create(**result)
    order.save()
    print("Added lab order:", order.id , "to the lab order table!\n")
    laborder_id += 1
  