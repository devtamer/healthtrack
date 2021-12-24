""" 
Defines Role Based Access Control for the System
"""
import enum
from re import A
from flask_marshmallow.schema import Schema

from marshmallow import fields 
from marshmallow_enum import EnumField

from api import db
from api.src.models.abstractmodel import BaseModel, MetaBaseModel
from api.src.models.mixin import RoleMixin


class AccessGroup(enum.Enum):
    ROOT = 1
    ADMIN = 2
    MED_ADMIN = 4
    MED_STAFF = 8
    LAB_ADMIN = 16
    LAB_STAFF = 32
    PHARM_ADMIN = 64
    PHARM_STAFF = 128


class AccessStatus(enum.Enum):
    DELETED = 1
    INACTIVE = 2
    ACTIVE = 4
    CANCELLED = 8
    PENDING = 16
    COMPLETE = 32

roles_parents = db.Table(
    'roles_parents',
    db.Column('role_id', db.Integer, db.ForeignKey('rolemodel.id')),
    db.Column('parent_id', db.Integer, db.ForeignKey('rolemodel.id')),
    extend_existing=True
)

class RoleModel(db.Model, RoleMixin, BaseModel, metaclass=MetaBaseModel ):
    __tablename__ = "rolemodel"
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), db.Identity(start=1), primary_key=True)
    name = db.Column(db.Enum(AccessGroup), unique=True, nullable=False)
    parents = db.relationship('RoleModel', 
                secondary=roles_parents,
                primaryjoin=(id == roles_parents.c.role_id),
                secondaryjoin=(id == roles_parents.c.parent_id),
                backref=db.backref('children', lazy='dynamic')
    )

    def __init__(self, name):
        RoleMixin.__init__(self)
        self.name = name

    def add_parent(self, parent):
        self.parents.append(parent)

    def add_parents(self, *parents):
        for parent in parents:
            self.add_parent(parent)
    
    @staticmethod
    def get_by_name(name):
        return RoleModel.query.filter_by(name=name).first()




