import unittest
from alchemytools.context import managed
from core.db.profile import Profile

from test import rebuild_schema
from core.action.stats import create
from core.db import Metadata, Session

__author__ = 'jesuejunior'
class ProfileTest(unittest.TestCase):

    def setUp(self):
        rebuild_schema(Metadata)

        self.data = {
            'username' : 'Batstaka',
            'url_stats' : 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/stats/327539077/ps3/',
            'url_weapons' : 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/weapons/327539077/ps3/',
            'url_vehicles': 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/vehicles/327539077/ps3/',
            }

    def tearDown(self):
        Metadata.drop_all()
        Metadata.create_all()

    def test_create_profile(self):
        create(self.data)
        with managed(Session) as session:

            profile = session.query(Profile).all()
            self.assertEquals(1, len(profile))

            self.assertEquals(profile[0].id, 1)
            self.assertEquals(profile[0].url_stats, 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/stats/327539077/ps3/')
            self.assertEquals(profile[0].url_weapons, 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/weapons/327539077/ps3/')
            self.assertEquals(profile[0].url_vehicles, 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/vehicles/327539077/ps3/')

    def test_profile_exist(self):
        create(self.data)
        with managed(Session) as session:
            profiles = session.query(Profile).all()
            self.assertEquals(1, len(profiles))

        create(self.data)
        with managed(Session) as session:
            profiles = session.query(Profile).all()
            self.assertEquals(1, len(profiles))
