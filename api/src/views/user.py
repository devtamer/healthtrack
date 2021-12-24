"""
Define the REST verbs for endpoints related to the User
"""
from re import I
from flask_cors import cross_origin
from flask.helpers import make_response
from flask.views import MethodView
from flask import json, jsonify, request
import jwt
from marshmallow import ValidationError
from marshmallow.decorators import VALIDATES
from webargs.flaskparser import abort, parser

import api.src.repositories.user as ur
import api.src.models.schema as s
import api.src.models.user as user


class RegisterAPI(MethodView):
    """ Resources for registering Users"""
    ur = ur.UserRepo()


    @staticmethod 
    @ur.token_required("ADMIN", "ROOT")
    @parser.use_kwargs(s.UserSchema(), location="json_or_form") 
    def post(email, password, roles):
        """
        Create User using all of the incoming information.
        Make sure user doesn't exist already. 
        """
        print("INCOMING ROLES:", roles)
        try:
            user = ur.UserRepo.get_by_email(email)
            response = {
                'Status': 'Fail',
                'Message': 'User with email ' + user.email +' already exists!'
            }
            return make_response(jsonify(response)), 202
        except ValidationError: 
            user = ur.UserRepo.create(email=email, password=password, roles=roles)
            response = {
                        'Status': 'Success',
                        'Message': 'User created with email: ' + user.email +
                        ', User ID: ' + str(user.id)
            }
            return make_response(jsonify(response)), 201
            


class LoginAPI(MethodView):
    """ Resources for Logging In"""
    ur = ur.UserRepo()

    @staticmethod
    @parser.use_kwargs(s.UserSchema(), location="json_or_form")
    def post(email, password):
        """Validate User Login Information & Generate JWT Token"""

        try:
            usr = ur.UserRepo.get_by_email(email) 
            print("USER ID", usr.id)
            ur.UserRepo.validate_password(usr, password)
            auth_token = usr.encode_auth_token(id=usr.id)
            if auth_token:
                response = {
                    'Status': 'Success',
                    'Message': 'Logged in!',
                    'auth_token': auth_token
                }
                return make_response(jsonify(response)), 200
        
        except ValidationError as err:
            print(err)
            response = {
                 'Status': 'Fail',
                 'Message': err.messages[0]
            }
            return make_response(jsonify(response)), 500

class StatusAPI(MethodView):
    """ Resources for verifying user status"""
    
    @staticmethod
    @ur.UserRepo.token_required()
    def get():
        auth_header = request.headers.get('Authorization')
        auth_token = auth_header.split(" ")[1]
        token_response = user.UserModel.decode_auth_token(auth_token)
        usr = ur.UserRepo.get_by_id(int(token_response))
        schema = s.UserSchema(exclude=["password"])
        data = schema.dump(usr) 
        return make_response(data), 200

class LogoutAPI(MethodView):
    """Resources for logging out"""
    urepo = ur.UserRepo()


    @urepo.token_required()
    def post(self):
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token = auth_header.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            token_reponse = user.UserModel.decode_auth_token(auth_token)
            if not isinstance(token_reponse, str):
                try:
                    ur.UserRepo.logout(auth_token)
                    response = {
                        'Status': 'Success',
                        'Message': 'You are now logged out!'
                    }
                    return make_response(jsonify(response)), 200
                except Exception as e:
                    response = {
                        'Status': 'Fail',
                        'Message': e,
                    }
                    return make_response(jsonify(response)), 200
            else:
                response = {
                    'Status': 'Fail',
                    'Message': auth_token
                }
                return make_response(jsonify(response)), 401
        else:
            response = {
                'Status': 'Fail',
                'Message': 'Provide a valid auth token.'
            }
            return make_response(jsonify(response)), 403

class UserProfileAPI(MethodView):
    """Resources for changing User Information"""
    
    @parser.use_kwargs(s.UserSchema(), location="json_or_form")
    def put(self, id, **kwargs):
        """Update any attribute of the User Model"""
        user = ur.UserRepo.get_by_id(id)
        
        return user