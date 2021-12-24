"""
Define the REST verbs for an appointment
"""
from flask.views import MethodView
from flask import jsonify
from webargs.flaskparser import parser


import api.src.repositories.appointment as ar
import api.src.models.schema as s


class AppointmentAPI(MethodView):
    """ Verbs that are relative to a lab"""
    

    @staticmethod
    def get(id):
        """ Return Appointment based on the id.

            If no appointment id is provided, all appointments will be returned.
        """

        if id is None:
            a = ar.AppointmentRepo.get_all()
            schema = s.AppointmentSchema(many=True)
            result = schema.load()

        else:
            p = ar.AppointmentRepo.get(id)
            print(p)
            schema = s.AppointmentSchema()
            print(schema)
       
        result = schema.dump(p)
    
        return result


    @staticmethod
    @parser.use_kwargs(s.AppointmentSchema, location="json_or_form")
    def post(id,**kwargs):
        """Create Appointment using all of the incoming information"""

        AppointmentRepo.create(id=id,**kwargs)

        return {'Status': 'Complete!'}, 201 # Will return some sort of message back to confirm that a user has been created?


    @parser.use_kwargs(s.AppointmentSchema, location="json_or_form")
    def put(id, **kwargs):
        """Update any attribute of the Appointment Model"""

        order = ar.AppointmentRepo.get(id)
        order.update(**kwargs)
        order.save()

        return {'Status': 'Complete!'}, 201