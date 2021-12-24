"""
Define the REST verbs
"""
from flask.views import MethodView
from flask import json, jsonify
from marshmallow import ValidationError
from marshmallow.utils import pprint
from webargs.flaskparser import use_kwargs

import api.src.repositories.equipment as eqrepo
import api.src.models.schema as s

class EquipmentAPI(MethodView):
    """ Verbs that are relative to equipment"""

    @staticmethod
    def get(id):
        """ Return equipment based on the id"""
        if id is None:
            e = eqrepo.EquipmentRepo.get_all()
            schema = s.EquipmentSchema(many=True)
            result = schema.load(e)
            return jsonify("Equipment:", result)
        else:
            p = eqrepo.EquipmentRepo.get(id)
            print(p)
            schema = s.EquipmentSchema()
            print(schema)
       
        result = schema.dump(p)
    
        return result

    @staticmethod
    @use_kwargs(s.EquipmentSchema())
    def post(**kwargs):
        """Create equipment using all of the incoming information"""
        schema = s.EquipmentSchema(missing=set)
        schema.load(**kwargs)
        return {'Status': 'Complete!'}, 201 # Will return some sort of message back to confirm that a user has been created?

    @use_kwargs
    def put(**kwargs):
        """Update any attribute of the Equipment Model"""
        pass