import api.src.models.medication as med
    
class MedicationRepo:

    @staticmethod
    def get(id):
        """ Query a piece of medication by id """
        return med.MedicationModel.query.filter_by(id=id).one_or_none()

    @staticmethod
    def get_all():
        """ Query all medication. Return a dictionary."""
        medication_list = med.MedicationModel.query.all()
        return medication_list
    
    @staticmethod
    def create(**kwargs):
        """ Create a new piece of medication"""

        eq = med.MedicationModel(**kwargs)
        return eq.save()
    
    def update(self,**kwargs):
        """ update any attribute of the medication"""
        for key, value in kwargs.items():
            locals()[key] = value