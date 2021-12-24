import os, sys
from re import A
import time
import json
import unittest
import requests


sys.path.append(os.path.abspath(os.path.join('../')))

from api.src.repositories.user import UserRepo
from api.src.views import physician
from api import db
from api.src.models.user import UserModel, BlacklistToken
from base import BaseTestCase



def register_user(self, email, password, role, headers):
    
    return self.client.post(
        '/admin/registeruser',
        data=json.dumps(dict(
            email=email,
            password=password,
            roles=role,
        )),
        headers=headers
    )

def login_user(self, email, password):
    return self.client.post(
        '/login/',
        data=json.dumps(dict(
            email=email,
            password=password
        )),
        content_type='application/json',
    )

def admin(self): 
    response = self.client.post(
    '/login/',
    data=json.dumps(dict(
        email='admin@admin.com',
        password='admin'
    )),
    content_type='application/json',
    )
    auth_token = response.json['auth_token']
    print('admin succesfully logged in')
    return auth_token   
    
     


class TestAuthBlueprint(BaseTestCase):

    #Test if admin account is created succesfully
    def testadmin(self):
        with self.client:
            print("RUNNING TEST ADMIN")
            admin(self)



    def test_registration(self):
        """ Test for user registration """
        with self.client:
            print("RUNNING REGISTRATION TEST")
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            print("HEADERS", headers)
            response = register_user(self, 'joe@gmail.com', '123456', ['MED_STAFF'], headers)
            print("RESPONSE IN TEST REG:", response)
            data = response.json
            print(data)
            self.assertTrue(data['Status'] == 'Success')
            self.assertTrue(data['Message'] == 'User created with email: joe@gmail.com, User ID: 2')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 201)

    def test_registered_with_already_registered_user(self):
        """ Test registration with already registered email"""
        user = UserModel(
            email='joe@gmail.com',
            password='test'
        )

        user.save()
        with self.client:
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            response = register_user(self, 'joe@gmail.com', '123456', ['MED_STAFF'], headers)
            data = response.json
            self.assertTrue(data['Status'] == 'Fail')
            self.assertTrue(data['Message'] == 'User with email joe@gmail.com already exists!')
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 202)

    def test_registered_user_login(self):
        """ Test for login of registered-user login """
        with self.client:
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            # user registration
            resp_register = register_user(self, 'joe@gmail.com', '123456',['MED_STAFF'], headers)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['Status'] == 'Success')
            self.assertTrue(data_register['Message'] == 'User created with email: joe@gmail.com, User ID: 2')
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # registered user login
            response = login_user(self, 'joe@gmail.com', '123456')
            data = response.json
            self.assertTrue(data['Status'] == 'Success')
            self.assertTrue(data['Message'] == 'Logged in!')
            self.assertTrue(data['auth_token'])
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 200)

    def test_non_registered_user_login(self):
        """ Test for login of non-registered user """
        with self.client:
            response = login_user(self, 'joe@gmail.com', '123456')
            data = response.json
            self.assertTrue(data['Status'] == 'Fail')
            self.assertTrue(data['Message'] == 'User does not exist!') 
            self.assertTrue(response.content_type == 'application/json')
            self.assertEqual(response.status_code, 500)

    def test_user_status(self):
        """ Test for user status """
        with self.client:
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            resp_register = register_user(self, 'joe@gmail.com', '123456',['MED_STAFF'], headers)
            response = login_user(self, 'joe@gmail.com', '123456')
            resp_payload = response.json
            payload = dict(
                first_name='Bob',
                last_name='Smith'
            )
            response = self.client.post(
                '/physicians/',
                data = payload, 
                headers=dict(
                    Authorization='Bearer ' + resp_payload['auth_token']
                )
            )
            data = response.json
            self.assertTrue(data['Status'] == 'Complete!')
            self.assertEqual(response.status_code, 201)

    def test_user_status_malformed_bearer_token(self):
        """ Test for user status with malformed bearer token"""
        with self.client:
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            resp_register = register_user(self, 'joe@gmail.com', '123456', ['LAB_ADMIN'], headers)
            response = login_user(self, 'joe@gmail.com', '123456')
            resp_payload = response.json
            payload = dict(
                first_name='Bob',
                last_name='Smith'
            )
            response = self.client.post(
              '/physicians/',
                data = payload, 
                headers=dict(
                    Authorization='Bearer ' + resp_payload['auth_token']
                )
            )
           
            self.assertEqual(response.status_code, 401)

    def test_valid_logout(self):
        """ Test for logout before token expires """
        with self.client:
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            # user registration
            resp_register = register_user(self, 'joe@gmail.com', '123456',['MED_STAFF'], headers)
            data_register = resp_register.json
            self.assertTrue(data_register['Status'] == 'Success')
            self.assertTrue(
                data_register['Message'] == 'User created with email: joe@gmail.com, User ID: 2')
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # user login
            resp_login = login_user(self, 'joe@gmail.com', '123456')
            data_login = resp_login.json
            self.assertTrue(data_login['Status'] == 'Success')
            self.assertTrue(data_login['Message'] == 'Logged in!')
            self.assertTrue(data_login['auth_token'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            # valid token logout
            response = self.client.post(
                '/dashboard/logout/',
                headers=dict(
                    Authorization='Bearer ' + data_login['auth_token']
                )
            )
            data = response.json
            self.assertTrue(data['Status'] == 'Success')
            self.assertTrue(data['Message'] == 'You are now logged out!')
            self.assertEqual(response.status_code, 200)

    def test_invalid_logout(self):
        """ Testing logout after the token expires """
        with self.client:
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            # user registration
            resp_register = register_user(self, 'joe@gmail.com', '123456', ['MED_STAFF'], headers)
            data_register = resp_register.json
            self.assertTrue(data_register['Status'] == 'Success')
            self.assertTrue(
                data_register['Message'] == 'User created with email: joe@gmail.com, User ID: 2')
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # user login
            resp_login = login_user(self, 'joe@gmail.com', '123456')
            data_login = json.loads(resp_login.data.decode())
            self.assertTrue(data_login['Status'] == 'Success')
            self.assertTrue(data_login['Message'] == 'Logged in!')
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            # invalid token logout
            response = self.client.post(
                '/dashboard/logout/',
            )
            data = response.json
            self.assertTrue(data['Status'] == 'Fail')
            self.assertTrue(
                data['Message'] == 'Provide a valid auth token.')
            self.assertEqual(response.status_code, 401)

    def test_valid_blacklisted_token_logout(self):
        """ Test for logout after a valid token gets blacklisted """
        with self.client:
            auth_token = "Bearer " + admin(self)
            headers = { 
                'Authorization': auth_token,
                'Content-Type': "application/json",
            }
            # user registration
            resp_register = register_user(self, 'joe@gmail.com', '123456', ['MED_STAFF'], headers)
            data_register = resp_register.json
            self.assertTrue(data_register['Status'] == 'Success')
            self.assertTrue(
                data_register['Message'] == 'User created with email: joe@gmail.com, User ID: 2')
            self.assertTrue(resp_register.content_type == 'application/json')
            self.assertEqual(resp_register.status_code, 201)
            # user login
            resp_login = login_user(self, 'joe@gmail.com', '123456')
            data_login = resp_login.json
            self.assertTrue(data_login['Status'] == 'Success')
            self.assertTrue(data_login['Message'] == 'Logged in!')
            self.assertTrue(data_login['auth_token'])
            self.assertTrue(resp_login.content_type == 'application/json')
            self.assertEqual(resp_login.status_code, 200)
            # blacklist a valid token
            blacklist_token = BlacklistToken(
                token=resp_login.json['auth_token'])
            db.session.add(blacklist_token)
            db.session.commit()
            # blacklisted valid token logout
            response = self.client.get(
                '/dashboard/logout/',
                headers=dict(
                    Authorization='Bearer ' + data_login['auth_token']
                )
            )
            data = response.json
            self.assertEqual(response.status_code, 405)



if __name__ == '__main__':
    unittest.main()