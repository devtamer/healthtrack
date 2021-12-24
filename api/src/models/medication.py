"""
Defines the model for a medication
"""
import enum
from flask_marshmallow.schema import Schema
from marshmallow import validate, pre_load, schema, fields
from marshmallow_enum import EnumField

from api import db
import api.src.models.abstractmodel as am
from sqlalchemy.orm import validates


#enumerate marketing status
class MarketingStatus(enum.Enum):
    Discontinued = "Discontinued"
    OTC = "Over-the-counter"
    Prescription = "Prescription"
    Notavail = "None (Tentative Approval)"

# just outlining the basic info needed that defines a medication 
# a more elegent approach will establish patients as objects in the system
class MedicationModel(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    __tablename__ = 'medicationmodel'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    owner = db.Column(db.Integer, default = 1, nullable=False)
    group = db.Column(db.Integer, default = 64, nullable=False) # default group is pharmacy admin
    status = db.Column(db.Integer, default = 4, nullable=False) # default status is active

    brand_name = db.Column(db.Text(), unique=False, nullable=False)
    reference_standard = db.Column(db.Text(), unique=False, nullable=True)
    dosage_form = db.Column(db.String(200), unique=False, nullable=True)
    route = db.Column(db.String(200), unique=False, nullable=True)
    marketing_status = db.Column(db.Enum(MarketingStatus), nullable= False)
    medicine_stock =  db.Column(db.Integer)
    
def __init__(self, id, brand_name, reference_standard, dosage_form, route, marketing_status):
        self.id = id
        self.brand_name = brand_name
        self.reference_standard = reference_standard
        self.dosage_form = dosage_form
        self.route = route
        self.marketing_status = marketing_status

