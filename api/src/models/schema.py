from flask_marshmallow.schema import Schema
from marshmallow import fields
from marshmallow_enum import EnumField

from api.src.models.employee import EmployeeType
from api.src.models.laborder import TestType
from api.src.models.medication import MarketingStatus


class RoleSchema(Schema):
    id = fields.Integer()
    name = fields.String()

class AppointmentSchema(Schema):
    id = fields.Integer()
    date = fields.Date()
    time = fields.Time()
    patient_id = fields.Integer()
    physician_id = fields.Integer()

class EmployeeSchema(Schema):
    id = fields.Integer()
    employee_type = EnumField(EmployeeType, error='by_name')
    first_name = fields.String()
    last_name = fields.String()
    start_date = fields.Date()
    number = fields.String()

class EquipmentSchema(Schema):
    id = fields.Integer()
    equipment_type = fields.String()
    description = fields.String()
    department = fields.String()
    own = fields.Boolean()
    purchase_date = fields.Date()



class MedicationSchema(Schema):
    brand_name = fields.String()
    reference_standard = fields.String()
    dosage_form = fields.String()
    route = fields.String()
    marketing_status = EnumField(MarketingStatus)
    medicine_stock = fields.Integer
        
class PatientSchema(Schema): 
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    number = fields.String()
    email = fields.Email()
    address = fields.String()
    insurance = fields.String()
    dob = fields.String()
    gender = fields.String()
    pcp_id = fields.Integer()
    medications = fields.String()
    appointments = fields.List(fields.Nested(AppointmentSchema()))

class PhysicianSchema(Schema):
    id = fields.Integer()
    first_name = fields.String()
    last_name = fields.String()
    number = fields.String()
    email = fields.Email()
    appointments = fields.List(fields.Nested(AppointmentSchema()))
    patients = fields.List(fields.Nested(PatientSchema()))
  

class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Email()
    password = fields.String()
    roles = fields.List(fields.String())
    registered_on = fields.DateTime()

class LabOrderSchema(Schema):
    test_type = EnumField(TestType, error='by_name') 
    id = fields.Integer()
    date_performed = fields.String()
    results = fields.String()
    performed_by = fields.String()
    tech_id = fields.Integer()
    patient_id = fields.Integer()
    physician_id = fields.Integer()
    patient = fields.Nested(PatientSchema())
    physician = fields.Nested(PhysicianSchema())

class PharmacyOrderSchema(Schema):

    id = fields.Integer()
    patient_id = fields.Integer()
    patient = fields.Nested(PatientSchema())
    pharmacist_id = fields.Integer()
    pharmacist = fields.Nested(EmployeeSchema())
    physician_id = fields.Integer()
    physician = fields.Nested(PhysicianSchema())
    medication = fields.String()
    dosage = fields.Integer()
    pickup_date = fields.String()
    filled_date = fields.String()

class UserSchema(Schema):
    id = fields.Integer()
    email = fields.Email()
    password = fields.String()
    roles = fields.List(fields.String())