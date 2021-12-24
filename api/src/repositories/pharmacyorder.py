"""
Class that allows interaction with the lab order database model
"""

import api.src.models.patient as patient
import api.src.models.pharmacyorder as po
import api.src.models.physician as md

class PharmacyOrderRepo():

    # Need to implement returning a list of results for the given search name. For now, this only returns a single result.
    # Implmentation should also suppport searching by any given attribute filter
    @staticmethod
    def get(id):
        """ Query a LabOrder by ID """
        return po.PharmacyOrderModel.query.filter_by(id=id).one_or_none()

    @staticmethod
    def get_all():
        """ Query all the LabOrders in the database. Return a dictionary."""
        order_list = po.PharmacyOrderModel.query.all()
        return order_list
    
    @staticmethod
    def create(**kwargs):
        """ Create a new LabOrder
            Must have a patient and physician associated upon creation    
        """
        # associated_physician = PhysicianModel.query.filter_by(id=physician_id).one()
        PharmacyOrder = po.PharmacyOrderModel(**kwargs)
        # LabOrder.append(associated_physician)
        if "patient_id" in kwargs:
            patient_id = kwargs.get("patient_id")
            associated_patient = patient.PatientModel.query.filter_by(id=patient_id).one()
            print("Retrieving patient...")
            PharmacyOrder.patient = associated_patient
            print("Pharmacy Order added to:", associated_patient.first_name, associated_patient.last_name)
            associated_patient.save()
        
        if "physician_id" in kwargs:
            physician_id = kwargs.get("physician_id")
            associated_md = md.PhysicianModel.query.filter_by(id=physician_id).one()
            PharmacyOrder.physician = associated_md
            associated_md.save()
        
        return PharmacyOrder.save()
    
    def update(self, **kwargs):
        """ update any attribute of the lab order"""
        for key, value in kwargs.items():
            locals()[key] = value
        
        return self

