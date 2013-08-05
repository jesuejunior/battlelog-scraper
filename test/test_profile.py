import unittest
from alchemytools.context import managed

from test import rebuild_schema
from core.action.profile import create, updater
from core.db import Metadata, Session
from core.db.profile import Profile

__author__ = 'jesuejunior'
class ProfileTest(unittest.TestCase):

    def setUp(self):
        rebuild_schema(Metadata)

        self.data = {
            'username' : 'Batstaka',
            'url_profile' : 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/stats/327539077/ps3/',
            'url_weapons' : 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/weapons/327539077/ps3/',
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
            self.assertEquals(profile[0].url_profile, 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/stats/327539077/ps3/')
            self.assertEquals(profile[0].url_weapons, 'http://battlelog.battlefield.com/bf3/soldier/Batstaka/weapons/327539077/ps3/')
    def test_profile_exist(self):
        create(self.data)
        with managed(Session) as session:
            profiles = session.query(Profile).all()
            self.assertEquals(1, len(profiles))

        create(self.data)
        with managed(Session) as session:
            profiles = session.query(Profile).all()
            self.assertEquals(1, len(profiles))


    def test_update_profile(self):

        create(self.data)

        profile_player = {
            'username' : 'Batstaka',
            'kills' : 16000,
            'deaths' : 12000,
            'kd_ratio' : 1.04,
            'kill_assists' : 1000,
            'score_min' : 550,
            'quits' : 30,
            'mcom_defend_kills' : 50,
            'mcom_destroyed' : 100,
            'flags_captured_conquest' : 120,
            'flags_defended_conquest' : 120,
            'vehicles_destroyed' : 2000,
            'vehicles_destroyed_assists' : 3000,
            'avg_weapon_accuracy' : 12.1,
            'longest_headshot' : 188,
            'highest_kill_streak' : 8,
            'skill' : 600,
            'avenger_kills' : 30,
            'savior_kills' : 20,
            'dogtags_taken' : 1600,
            'flags_captured_ctf' : 35,
            'squad_score_bonus' : 599,
            'repairs' : 1200,
            'revives' : 5000,
            'heals' : 20000,
            'resupplies' : 300,
            'shots_fired' : 222,
            'highest_nemesis_streak' : 9,
            'nemesis_kills' : 21,
            'suppression_assists' : 123,
        }


        with managed(Session) as session:

            p1 = session.query(Profile).filter_by(username='Batstaka')[0]

            self.assertEquals(p1.username, 'Batstaka')
            self.assertEquals(p1.kills, 0)
            self.assertEquals(p1.deaths, 0)
            self.assertEquals(p1.kd_ratio, 0.0)
            self.assertEquals(p1.kill_assists, 0)
            self.assertEquals(p1.score_min, 0)

            updater(profile_player)

        with managed(Session) as session:
            p_test = session.query(Profile).filter_by(username='Batstaka')[0]

            self.assertEquals(p_test.kills, 16000)
            self.assertEquals(p_test.deaths, 12000)
            self.assertEquals(p_test.kd_ratio, 1.04)
            self.assertEquals(p_test.kill_assists, 1000)
            self.assertEquals(p_test.score_min, 550)
            self.assertEquals(p_test.quits, 30)
            self.assertEquals(p_test.mcom_defend_kills, 50)
            self.assertEquals(p_test.mcom_destroyed, 100)
            self.assertEquals(p_test.flags_captured_conquest, 120)
            self.assertEquals(p_test.flags_defended_conquest, 120)
            self.assertEquals(p_test.vehicles_destroyed, 2000)
            self.assertEquals(p_test.vehicles_destroyed_assists, 3000)
            self.assertEquals(p_test.avg_weapon_accuracy, 12.1)
            self.assertEquals(p_test.longest_headshot, 188)
            self.assertEquals(p_test.highest_kill_streak, 8)
            self.assertEquals(p_test.skill, 600)
            self.assertEquals(p_test.avenger_kills, 30)
            self.assertEquals(p_test.savior_kills, 20)
            self.assertEquals(p_test.dogtags_taken, 1600)
            self.assertEquals(p_test.flags_captured_ctf, 35)
            self.assertEquals(p_test.squad_score_bonus, 599)
            self.assertEquals(p_test.repairs, 1200)
            self.assertEquals(p_test.revives, 5000)
            self.assertEquals(p_test.heals, 20000)
            self.assertEquals(p_test.resupplies, 300)
            self.assertEquals(p_test.shots_fired, 222)
            self.assertEquals(p_test.highest_nemesis_streak, 9)
            self.assertEquals(p_test.nemesis_kills, 21)
            self.assertEquals(p_test.suppression_assists, 123)