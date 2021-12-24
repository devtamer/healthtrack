"""
Create a database column that does not allow any updates.
https://stackoverflow.com/questions/34953759/make-a-column-immutable-in-sqlalchemy
"""

from sqlalchemy import event
from sqlalchemy.util.langhelpers import symbol


class NonUpdateableColumnError(AttributeError):
    def __init__(self, cls, column, old_value, new_value, message=None):
        self.cls = cls
        self.column = column
        self.old_value = old_value
        self.new_value = new_value

        if message is None:
            self.message = 'Cannot update column {} on model {} from {} to {}: column is non-updateable.'.format(
                column, cls, old_value, new_value)


def make_immutable(col):
    @event.listens_for(col, 'set')
    def unupdateable_column_set_listener(target, value, old_value, initiator):
        if old_value != symbol('NEVER_SET') and old_value != symbol('NO_VALUE') and old_value != value:
            raise NonUpdateableColumnError(col.class_.__name__, col.name, old_value, value)