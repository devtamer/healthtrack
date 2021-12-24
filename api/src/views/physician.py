"""
Define the REST verbs for endpoints related to a Physician
"""
from re import M
from flask.views import MethodView
from flask import json, jsonify
from flask_cors.decorator import cross_origin
from marshmallow import ValidationError
from marshmallow.decorators import VALIDATES
from marshmallow.utils import pprint
from webargs.flaskparser import abort, parser

import api.src.repositories.user as ur
import api.src.repositories.physician as pr
import api.src.models.schema as s

class PhysicianAPI(MethodView):
    """ Verbs that are relative to the Physicians"""
    ur = ur.UserRepo()

    @staticmethod
    @ur.token_required()
    def get(id):
        """ Return a physician based on the id"""
        if id is None: 
            p = pr.PhysicianRepo.get_all()
            schema = s.PhysicianSchema(many=True)
            result = schema.dump(p, many=True)
            return jsonify({"Physicians": result})

        else:
            p = pr.PhysicianRepo.get(id)
            schema = s.PhysicianSchema()
            result = schema.dump(p)
       
        return result


    @staticmethod
    @ur.token_required("ROOT", "ADMIN", "MED_ADMIN", "MED_STAFF")
    @parser.use_kwargs(s.PhysicianSchema, location="json_or_form") 
    def post(**kwargs):
        """Create Physician using all of the incoming information"""

        pr.PhysicianRepo.create(**kwargs)

        return {'Status': 'Complete!'}, 201 # Will return some sort of message back to confirm that a user has been created?


    @ur.token_required("ROOT", "ADMIN", "MED_ADMIN", "MED_STAFF")
    @parser.use_kwargs(s.PhysicianSchema, location="json_or_form") 
    def put(self, id, **kwargs):
        """Update any attribute of the Physician Model"""
        physician = pr.PhysicianRepo.get(id)
        updated_md = pr.PhysicianRepo.update(id, **kwargs)

        return jsonify({'Updated': (updated_md.first_name, updated_md.last_name)}), 201