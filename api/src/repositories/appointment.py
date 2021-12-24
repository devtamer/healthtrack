from api.src.models.appointment import AppointmentModel
from api.src.models.patient import PatientModel
from api.src.models.physician import PhysicianModel

class AppointmentRepo():

    # Need to implement returning a list of results for the given search name. For now, this only returns a single result.
    # Implmentation should also suppport searching by any given attribute filter
    @staticmethod
    def get(id):
        """ Query a Appointment by ID """
        return AppointmentModel.query.filter_by(id=id).one_or_none()

    @staticmethod
    def get_all():
        """ Query all the Appointments in the database. Return a dictionary."""
        appointment_list = AppointmentModel.query.all()
        return appointment_list
    
    @staticmethod
    def create(**kwargs):
        """ Create a new Appointment"""
        Appointment = AppointmentModel(**kwargs)

        if "patient_id" in kwargs:
            patient_id = kwargs.get("patient_id")
            patient = PatientModel.query.filter_by(id=patient_id).one()
            patient.appointments.append(Appointment)
            patient.save()

        if "physician_id" in kwargs:
            physician_id = kwargs.get("physician_id")
            physician = PhysicianModel.query.filter_by(id=physician_id).one()
            physician.appointments.append(Appointment)
            physician.save()

        return Appointment.save()
    

    # Need to implement a way to remove an appointment from a doctor's schedule if the appointment gets changed
    # to another doctor or deleted
    def update(self, id, **kwargs):
        """ update any attribute of the appointment"""
        Appointment = self.get(id)
        for key, value in kwargs.items():
            setattr(Appointment, key, value)

        # Update the attending doctor 
        if "physician_id" in kwargs:
            physician_id = kwargs.get("physician_id")
            physician = PhysicianModel.get(id=physician_id)
            physician.Appointments.append(Appointment)

        return Appointment.save()
    
    