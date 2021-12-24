import api.src.models.physician as md

class PhysicianRepo():

    # Need to implement returning a list of results for the given search name. For now, this only returns a single result.
    # Implmentation should also suppport searching by any given attribute filter
    @staticmethod
    def get(id):
        """ Query a Physician by ID """
        return md.PhysicianModel.query.filter_by(id=id).one_or_none()

    @staticmethod
    def get_all():
        """ Query all the Physicians in the database. Return a dictionary."""
        print("Querying physician table...")
        Physician_list = md.PhysicianModel.query.all()

        return Physician_list
    
    @staticmethod
    def create(**kwargs):
        """ Create a new Physician"""
        Physician = md.PhysicianModel(**kwargs)
        return Physician.save()
    
    def update(self, id, **kwargs):
        """ update any attribute of the user"""
        physician = self.get(id)
        for key, value in kwargs.items():
            setattr(physician, key, value)
        
        return physician.save()