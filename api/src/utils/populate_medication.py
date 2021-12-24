import json
import inspect
from re import I, U
import sys, os
import random
from marshmallow.utils import pprint
import requests
import webargs

# add app path 
sys.path.append(os.path.abspath(os.path.join('../../..')))


from api.src.models.medication import MedicationModel, MedicationSchema
from api import create_app

app=create_app()
app.app_context().push()

with open("mock_data/drugs.json") as drugs:
    data = json.load(drugs)

for sub in data['results']:
    if 'products' in sub.keys():
        added = []
        for p in sub['products']:
             if p['brand_name'] not in added:
                    brand = p['brand_name']
                    added.append(brand)
                    ref = p['reference_drug']
                    
                    ref_std = p['reference_standard'] if 'reference_standard' in p.keys() else 'No'
                    dosage = p['dosage_form']
                    roa = p['route']

                    if p['marketing_status'] == "Discontinued":
                        mkt_status="Discontinued"
                    elif p['marketing_status'] == "Over-the-counter":
                        mkt_status="OTC"
                    elif p['marketing_status'] == "Prescription":
                        mkt_status="Prescription"
                    else:
                        mkt_status="Notavail"

                    med = MedicationModel(brand_name=brand,reference_standard=ref_std,
                                            dosage_form=dosage, route=roa,
                                            marketing_status=mkt_status)
                    med.save()



     