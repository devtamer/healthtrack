

import unittest

from flask import current_app
from flask_testing import TestCase
from api.config import DevelopmentConfig
from api.config import TestingConfig

from api import app
from api import create_app

app = create_app()

class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object(DevelopmentConfig)
        return app

    def test_app_is_development(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'SECRET')
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:SanFran!10@localhost/health'
        )


class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('') 
        return app

    def test_app_is_testing(self):
        self.assertFalse(app.config['SECRET_KEY'] is 'SECRET')
        self.assertTrue(app.config['DEBUG'])
        self.assertTrue(
            app.config['SQLALCHEMY_DATABASE_URI'] == 'postgresql://postgres:SanFran!10@localhost/health'
        )


class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object(TestingConfig)
        return app

    def test_app_is_production(self):
        self.assertTrue(app.config['DEBUG'] is False)


if __name__ == '__main__':
    unittest.main()