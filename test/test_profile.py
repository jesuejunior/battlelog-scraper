import unittest
from alchemytools.context import managed
from core.action.profile import create
from core.db import Metadata, Session
from core.db.profile import Profile

__author__ = 'jesuejunior'
class ProfileTest(unittest.TestCase):

    def setUp(self):
        Metadata.drop_all()
        Metadata.create_all()

        self.data = {
            'username' : 'Batstaka',
            'url_profile' : 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/stats/327539077/ps3/',
            'url_weapons' : 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/weapons/327539077/ps3/',
            }

    def tearDown(self):
        Metadata.drop_all()
        Metadata.create_all()

    def test_new_profile(self):
        with managed(Session) as session:
            create(self.data)

            profile = session.query(Profile).all()
            self.assertEquals(1, len(profile))

            self.assertEquals(profile[0].id, 1)
            self.assertEquals(profile[0].url_profile, 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/stats/327539077/ps3/')
            self.assertEquals(profile[0].url_weapons, 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/weapons/327539077/ps3/')