"""
Define the REST verbs for endpoints related to a pharmacy order 
"""
from flask.views import MethodView
from flask import json, jsonify
from marshmallow import ValidationError
from marshmallow.decorators import VALIDATES
from marshmallow.utils import pprint
from webargs.flaskparser import abort, parser, use_kwargs, use_args

import api.src.repositories.pharmacyorder as por
import api.src.models.schema as s
import api.src.repositories.user as ur

class PharmacyOrderAPI(MethodView):
    """ Verbs that are relative to the PharmacyOrders"""
    ur = ur.UserRepo()

    @staticmethod
    @ur.token_required()
    def get(id):
        """ Return a pharmacy order based on the id"""
        if id is None:
            p = por.PharmacyOrderRepo.get_all()
            schema = s.PharmacyOrderSchema(many=True)
            result = schema.dump(p)
            return jsonify({"PharmacyOrders": result})
        else:
            p = por.PharmacyOrderRepo.get(id)
            print(p)
            schema = s.PharmacyOrderSchema()
            print(schema)
       
        result = schema.dump(p)
    
        return result

    @staticmethod
    @ur.token_required()
    @parser.use_kwargs(s.PharmacyOrderSchema(), location="json_or_form") 
    def post(**kwargs):
        """Create PharmacyOrder using all of the incoming information"""
        por.PharmacyOrderRepo.create(**kwargs)

        return {'Status': 'Complete!'}, 201 

    @staticmethod
    @ur.token_required()
    @parser.use_kwargs(s.PharmacyOrderSchema(), location="json_or_form")
    def put(id, **kwargs):
        """Update any attribute of the PharmacyOrder Model"""
        repository = por.PharmacyOrderRepo()
        updated_PharmacyOrder = repository.update(id, **kwargs)

        return jsonify({'Updated': (updated_PharmacyOrder.first_name, updated_PharmacyOrder.last_name)}), 201