from flask.helpers import make_response
from flask import jsonify, request
from functools import wraps
import webargs
from webargs.flaskparser import abort
from api import bcrypt
from webargs import ValidationError

import api.src.models.employee as emp

class EmployeeRepo():
 
    @staticmethod
    def get_by_id(id):
        """ Query a User by their id"""
        employee = emp.EmployeeModel.query.filter_by(id=id).one_or_none()
        if employee is None:
            raise ValidationError("Employee does not exist!")
        
        return employee

    @staticmethod
    def get_user_info(id=None, model=None):
        """Retrieves login email and associated user id of the employee 
        
        If no keyword arguments are passed in, None will be returned

        Parameters
        ----------
        id : int, optional
            The id of the employee
        model : EmployeeModel, optional
            The EmployeeModel object for the employee
        
        Returns
        -------
        str, int
            The login email and user id associated with the employee
        """


        if id:
            employee = EmployeeRepo.get_by_id(id)
            user = employee.user
            return user.email, user.id
        elif model:
            user = model.user
            return user.email, user.id
        else:
            print("USER INFO RETRIEVAL ERROR: No info was provided.")
            return None


    @staticmethod
    def get_all():
        """ Query all the Users in the database. Return a dictionary."""

        print("Querying User table...")
        Employee_list = emp.EmployeeModel.query.all()

        return Employee_list
    
    @staticmethod
    def create(**kwargs):
        """ Create a new employee"""
        
        employee = emp.EmployeeModel(**kwargs)
    
        return employee.save()
 
 
    def update(self, id, **kwargs):
        """ Update any attribute of the employee"""

        Employee = self.get_by_id(id)
        for key, value in kwargs.items():
            setattr(Employee, key, value)
        
        return Employee.save()
    
    
        
