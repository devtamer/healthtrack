from re import I
import uuid

from api.src.models.access import AccessGroup, RoleModel
from api.src.models.user import UserModel
from api import db

# must be used within an app context
def create_roles():
    """ Used within :obj:`manage.py` """
    print("Adding access roles to database...")
    for group in AccessGroup:
        role = RoleModel(str(group.name))
        role.save()
    

# must be used within an app context
def create_admin(email="admin@admin.com", password="admin"):
    """Creates an root admin. Used within :obj:`manage.py`"""

    admin = UserModel(
            email=email,
            password=password,
        ) 

    admin.add_role("ROOT") 
    print("Adding root admin...")
    admin.save()
    print(f"ROOT Admin added with credentials:\n email: {email}\n password: {password}")

# implement a unique ID generator here
def generate_id():
    pass