"""Message model tests."""

# run these tests like:
#
#    python -m unittest test_user_model.py


import os
from unittest import TestCase

from models import db, Message

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///warbler_test"

# Now we can import app

from app import app

# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.drop_all()
db.create_all()


class MessageModelTestCase(TestCase):
    def setUp(self):
        Message.query.delete()

        m1 = Message.signup("m1", "m1@email.com", "password", None)
        m2 = Message.signup("m2", "m2@email.com", "password", None)

        db.session.commit()
        self.m1_id = m1.id
        self.m2_id = m2.id

        self.client = app.test_client()

    def tearDown(self):
        db.session.rollback()

    def test_message_model(self):
        """Verify that models have the attributes you expect"""
        """write tests for any model methods"""