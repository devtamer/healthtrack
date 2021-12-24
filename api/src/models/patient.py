"""
Defines the model for a patient
"""

from flask_marshmallow.schema import Schema
from marshmallow import fields


import api.src.models.abstractmodel as am
import api.src.models.laborder as lo
import api.src.models.appointment as appt
from api.src.utils.stripped_string import StrippedString
from api import db


class PatientModel(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    __tablename__ = 'patientmodel'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    owner = db.Column(db.Integer, default = 1, nullable=False)
    group = db.Column(db.Integer, default = 8, nullable=False) # default group is medical staff
    status = db.Column(db.Integer, default = 0, nullable=False) # status irrelevant 

    first_name = db.Column(StrippedString(120), unique=False, nullable=False)
    last_name = db.Column(StrippedString(120), unique=False, nullable=False)
    number = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(StrippedString(50), unique=True, nullable= True)
    address = db.Column(db.String(200), unique=False, nullable=True)
    insurance = db.Column(db.String(50), unique=False, nullable=True)
    dob = db.Column(db.String(20), unique=False, nullable=True)
    gender = db.Column(db.String(20), unique=False, nullable=True)
    medications = db.Column(db.String(200), unique=False, nullable=True) # need to implement a one to many relationship for a Patient model to Medication models

    # foreign keys
    pcp_id = db.Column(db.Integer, db.ForeignKey("physicianmodel.id"))

    # relationships
    appointments = db.relationship("AppointmentModel", cascade="all,delete",backref="patientmodel", lazy=True)

    def __init__(self, first_name, last_name, number, email="",
                    address="", insurance="", dob="", gender="", pcp_id="", 
                    medications="", appointments=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.email = email
        self.address = address
        self.insurance = insurance
        self.dob = dob
        self.gender = gender
        self.pcp = pcp_id
        self.medications = medications
        self.appointments = appointments 





    
    

