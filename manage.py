"""
Manager script for testing and database utilities
Implemenation adapted from https://github.com/realpython/flask-jwt-auth
"""

from flask_script import Manager

from api import create_app, db
from api.src.utils.utilities import create_roles, create_admin


manager = Manager(create_app)

@manager.command
def create_db():
    """Creates the db tables"""
    print("Creating database tables...")
    db.create_all()
    create_roles()
    create_admin()


@manager.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()

@manager.command
def refresh_db():
    """Drops & Recreates db tables"""
    print("Recreating Database...")
    drop_db()
    print("Tables dropped...")
    create_db()

@manager.command
def populate_db():
    import api.src.utils.populate_db as pop_db
    pop_db

if __name__ == '__main__':
    manager.run()