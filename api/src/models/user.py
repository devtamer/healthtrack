"""
Defines Model for a User and Defines Methods for JWT Use
"""
from re import A
from flask.helpers import make_response
from flask.json import jsonify
from marshmallow import Schema, fields
from sqlalchemy.orm import backref
from sqlalchemy.sql import func
from flask import current_app
import jwt, datetime

from webargs.flaskparser import abort

from api import db
from api import bcrypt

from api.src.utils.stripped_string import StrippedString
import api.src.models.access as access
import api.src.models.abstractmodel as am

users_roles = db.Table(
    'users_roles',
    db.Column('user_email', db.String, db.ForeignKey('usermodel.email')),
    db.Column('role_name', db.Enum(access.AccessGroup), db.ForeignKey('rolemodel.name'))
)

class UserModel(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    __tablename__ = 'usermodel'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, db.Identity(start=1), primary_key=True)
    status = db.Column(db.Enum(access.AccessStatus), default = "ACTIVE", nullable=False) # default status active
    email = db.Column(StrippedString(50), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False) # store the hashed password
    created = db.Column(db.DateTime(timezone=True), server_default=func.now())

    roles = db.relationship('RoleModel', 
            secondary=users_roles,cascade="all,delete",
            backref=backref('roles', cascade="all,delete",lazy='dynamic')
    )

    def __init__(self, email, password, roles=[]):
        self.email = email
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')
        for role in roles:
            self.add_role(role)


    def add_role(self, rolename):
        role = access.RoleModel.get_by_name(rolename)
        self.roles.append(role)
    

    def add_roles(self, *roles):
        for role in roles:
            self.add_roles(role)

    def get_roles(self):
        all_roles = []
        for role in self.roles:
            all_roles.append(role.name.name)
        print("Roles retrieved:", all_roles) 

        return all_roles

        

    def encode_auth_token(self, id):
        """
        Genereates JWT Auth Token
        :return: string
        """

        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=60),
                'iat': datetime.datetime.utcnow(),
                'sub': id
            }
            return jwt.encode(
                payload,
                current_app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(auth_token):
        """
        Decodes JWT Toekn
        :param auth_token:
        :return: integer|string
        """

        try:
            payload = jwt.decode(auth_token, current_app.config.get('SECRET_KEY'), algorithms=["HS256"])
            is_blacklisted = BlacklistToken.check_blacklist(auth_token)
            if is_blacklisted:
                return 'Token Blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            message = {
                'Status': 'Fail',
                'Message': 'Signature Expired. Please log in again.'
            }
            return abort(401, make_response(jsonify(message)))

        except jwt.InvalidTokenError:
            return abort(401, 'Invalid Token. Please log in again.')



class BlacklistToken(db.Model, am.BaseModel, metaclass=am.MetaBaseModel):
    """
    Token Model for storing JWT Tokens
    """
    __tablename__ = 'blacklist_tokens'

    id = db.Column(db.Integer, primary_key=True) # Need to setup autoincrement of id
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()
    
    def __repr__(self):
        return '<id: token: {}'.format(self.token)

    def check_blacklist(auth_token):
        # check whether auth token has been blacklisted
        result = BlacklistToken.query.filter_by(token=str(auth_token)).first()
        if result:
            return True
        else:
            return False

