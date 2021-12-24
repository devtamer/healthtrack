"""
Define the REST verbs for endpoints related to a patient
"""
from flask.views import MethodView
from flask import json, jsonify
from marshmallow import ValidationError
from marshmallow.decorators import VALIDATES
from marshmallow.utils import pprint
from webargs.flaskparser import abort, parser, use_kwargs, use_args

import api.src.repositories.patient as pr
import api.src.models.schema as s
import api.src.repositories.user as ur

class PatientAPI(MethodView):
    """ Verbs that are relative to the patients"""
    ur = ur.UserRepo()

    @staticmethod
    @ur.token_required()
    def get(id):
        """ Return a user based on the id"""
        if id is None:
            p = pr.PatientRepo.get_all()
            schema = s.PatientSchema(many=True)
            result = schema.dump(p)
            return jsonify({"Patients": result})
        else:
            p = pr.PatientRepo.get(id)
            print(p)
            schema = s.PatientSchema()
            print(schema)
       
        result = schema.dump(p)
    
        return result

    @staticmethod
    @ur.token_required()
    @parser.use_kwargs(s.PatientSchema(), location="json_or_form") 
    def post(**kwargs):
        """Create patient using all of the incoming information"""
        pr.PatientRepo.create(**kwargs)

        return {'Status': 'Complete!'}, 201 

    @staticmethod
    @ur.token_required()
    @parser.use_kwargs(s.PatientSchema(), location="json_or_form")
    def put(id, **kwargs):
        """Update any attribute of the Patient Model"""
        repository = pr.PatientRepo()
        updated_patient = repository.update(id, **kwargs)

        return jsonify({'Updated': (updated_patient.first_name, updated_patient.last_name)}), 201