import api.src.models.equipment as eq  
    
class EquipmentRepo:

    @staticmethod
    def get(id):
        """ Query a piece of equipment by id """

        return eq.EquipmentModel.query.filter_by(id=id).one_or_none()

    @staticmethod
    def get_all():
        """ Query all equipment. Return a dictionary."""

        patient_list = eq.EquipmentModel.query.all()
        
        return patient_list
    
    @staticmethod
    def create(**kwargs):
        """ Create a new piece of equipment"""

        equipment = eq.EquipmentModel(**kwargs)

        return equipment.save()
    
    def update(self,**kwargs):
        """ update any attribute of the user"""

        for key, value in kwargs.items():
            locals()[key] = value