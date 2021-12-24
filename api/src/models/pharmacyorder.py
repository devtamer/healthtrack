"""
Define the model for pharmacy order
"""
import enum
import datetime
from flask_marshmallow.schema import Schema
from marshmallow import validate, pre_load, schema, fields, ValidationError
from marshmallow_enum import EnumField
from sqlalchemy.sql.functions import func

from api import db, ma
import api.src.models.abstractmodel as am
import api.src.models.employee as emp
import api.src.models.patient as patient
import api.src.models.physician as md

from sqlalchemy.orm import backref, validates

class PharmacyOrderModel(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    __tablename__ = 'pharmacyordermodel'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    owner = db.Column(db.Integer, default = 1, nullable=False)
    group = db.Column(db.Integer, default = 128, nullable=False) # default group is pharmacy staff
    status = db.Column(db.Integer, default = 4, nullable=False) # default status active

    patient_id = db.Column(db.Integer, db.ForeignKey('patientmodel.id'))
    patient = db.relationship("PatientModel", cascade="all,delete",backref="pharmacyordermodel",lazy=True)
    physician_id = db.Column(db.Integer, db.ForeignKey('physicianmodel.id'))
    physician = db.relationship("PhysicianModel", cascade="all,delete",backref="pharmacyordermodel",lazy=True)
    # medication = db.Column(db.String(64), db.ForeignKey('medicationmodel.id'))
    
    dosage = db.Column(db.Integer, nullable=True)
    order_date = db.Column(db.Date,server_default=func.now())
    pickup_date = db.Column(db.Date, nullable=True) 
    filled_date = db.Column(db.Date, nullable=True)
    pharmacist_id = db.Column(db.Integer, db.ForeignKey('employeemodel.id'), nullable=True)
    pharmacist = db.relationship("EmployeeModel", cascade="all,delete",backref=backref("pharmacyordermodel", uselist=False))
    
    def __init__(self, patient_id,physician_id,dosage=None, pickup_date=None, filled_date=None, pharmacist=None, physician=None):
        self.patient_id = patient_id
        self.physician_id = physician_id
        self.dosage = dosage 
        self.pickup_date = pickup_date
        self.filled_date = filled_date
        


    @validates("pharmacist")
    def validate_pharmacist(self, pharmd):
        if pharmd:
            if pharmd['employee_type'] != 'PHARM_ADMIN':
                raise ValidationError("Must be a pharmacist!")


    


