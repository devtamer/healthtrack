from flask_testing import TestCase

from api.config import TestingConfig
from api import db
from api import create_app
from api.src.utils.utilities import create_admin, create_roles


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        app = create_app(TestingConfig)
        return app
        
    def setUp(self):
        db.create_all(app = create_app(TestingConfig))
        create_roles()
        create_admin()

    def tearDown(self):
        db.session.remove()
        db.drop_all()