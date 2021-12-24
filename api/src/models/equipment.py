from operator import eq
from marshmallow import Schema
from marshmallow import fields
from marshmallow.fields import Email
import enum 

from api import db
import api.src.models.abstractmodel as am


class Department(enum.Enum):
    MD = "Medical Department"
    LD = "Lab Department"
    PD = "Pharmacy Department"
    AD = "Admin Department"

class EquipmentModel(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    __tablename__ = 'equipmentmodel'

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    owner = db.Column(db.Integer, default = 1, nullable=False)
    group = db.Column(db.Integer, default = 1, nullable=False)
    status = db.Column(db.Integer, default = 4, nullable=False) # default status is active

    equipment_type = db.Column(db.String(20), unique=False, nullable=False)
    description = db.Column(db.String(200), unique=False, nullable=False)
    department = db.Column(db.Enum(Department), nullable=False)    
    own = db.Column(db.Boolean, unique=False, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)

    def __init__(self, id, equipment_type, description, department, own, purchase_date):
        self.id = id
        self.equipment_type = equipment_type
        self.description = description
        self.department = department
        self.own = own
        self.purchase_date = purchase_date



