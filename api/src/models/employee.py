"""
Define the model for an employee
"""
import enum
from marshmallow import fields, Schema
from marshmallow_enum import EnumField
from sqlalchemy.orm import backref, validates
from sqlalchemy.sql.functions import func
from sqlalchemy.types import TypeDecorator



from api import db, ma
import api.src.models.abstractmodel as am
from api.src.utils.stripped_string import StrippedString
class EmployeeType(enum.Enum):
    PA = "Phsyician's Assistant"
    RN = "Nurse"
    MA = "Medical Assistant"
    PD = "Pharamacist"
    LT = "Lab Technician"


class EmployeeModel(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    __tablename__ = 'employeemodel'
    __table_args__ = {'extend_existing':True}

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    owner = db.Column(db.Integer, default = 1, nullable=False)
    group = db.Column(db.Integer, default = 1, nullable=False)
    status = db.Column(db.Integer, default = 4, nullable=False) # default status is active

    employee_type = db.Column(db.Enum(EmployeeType), nullable=False)
    first_name = db.Column(StrippedString(50), nullable=False)
    last_name = db.Column(StrippedString(50), nullable=False)
    start_date = db.Column(db.Date,server_default=func.now())
    number = db.Column(StrippedString(15), nullable=True)        # nullable=False for production
   
    # relationships
    user_id = db.Column(db.Integer, db.ForeignKey('usermodel.id'))
    user = db.relationship("UserModel",backref=backref("employeemodel", cascade="all,delete",uselist=False))
    lab_orders = db.relationship("LabOrderModel", cascade="all,delete",backref="employeemodel", lazy='select')
    
    
    def __init__(self, employee_type, first_name, last_name, number=""):
        self.employee_type = employee_type
        self.first_name = first_name
        self.last_name = last_name
        self.number = number

    

   



