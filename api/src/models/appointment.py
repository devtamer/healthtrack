"""
Defines model and schema for appointments
"""
from flask_marshmallow.schema import Schema
from marshmallow import fields

import api.src.models.abstractmodel as am
from api import db

class AppointmentModel(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    __tablename__ = 'appointmentmodel'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    owner = db.Column(db.Integer, default = 1, nullable=False)
    group = db.Column(db.Integer, default = 8, nullable=False) # default group is medical staff
    status = db.Column(db.Integer, default = 4, nullable=False) # default status is active

    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time(timezone=True), nullable=False)
    
    # relationships (1 to 1)
    patient_id = db.Column(db.Integer, db.ForeignKey('patientmodel.id'))
    physician_id = db.Column(db.Integer, db.ForeignKey('physicianmodel.id'))

    def __init__(self, id, date, time, patient_id="", phsyician_id=""):
        self.id = id
        self.date = date
        self.time = time
        self.patient_id = patient_id
        self.physician_id = phsyician_id

