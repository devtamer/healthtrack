import  api.src.models.patient as patient
import  api.src.repositories.physician as mdrepo

class PatientRepo():

    # Need to implement returning a list of results for the given search name. For now, this only returns a single result.
    # Implmentation should also suppport searching by any given attribute filter
    @staticmethod
    def get(id):
        """ Query a patient by ID """
        return patient.PatientModel.query.filter_by(id=id).one_or_none()

    @staticmethod
    def get_all():
        """ Query all the patients in the database. Return a dictionary."""
        patient_list = patient.PatientModel.query.all()
        return patient_list
    
    @staticmethod
    def create(**kwargs):
        """ Create a new patient"""
        pt = patient.PatientModel(**kwargs)
        if "pcp_id" in kwargs:
            physician_id = kwargs.get("pcp_id")
            physician = mdrepo.PhysicianRepo.get(id=physician_id)
            physician.patients.append(pt)
            physician.save()
        
        return pt.save()
    

    def update(self, id, **kwargs):
        """ update any attribute of the user"""
        patient = self.get(id)
        for key, value in kwargs.items():
            setattr(patient, key, value)

        if "physician_id" in kwargs:
            physician_id = kwargs.get("physician_id")
            physician = mdrepo.PhysicianRepo.get(id=physician_id)
            physician.patients.append(patient)
            physician.save()

        return patient.save()
    
    