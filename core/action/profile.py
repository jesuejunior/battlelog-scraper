from alchemytools.context import managed
from core.db import Session
from core.db.profile import Profile

__author__ = 'jesuejunior'

def create(data):

    with managed(Session) as session:
        try:
            valid = session.query(Profile).filter_by(username=data['username'])[0]
        except Exception:
            valid = False
    if valid:
        return False
    else:
        with managed(Session) as session:
            profile = Profile(username=data['username'], url_profile=data['url_profile'], url_weapons=data['url_weapons'] )
            session.add(profile)
        return True

def updater(data):
    with managed(Session) as session:
        profile = session.query(Profile).filter_by(username=data['username'])[0]

        profile.kills = data['kills']
        profile.deaths = data['deaths']
        profile.kd_ratio = data['kd_ratio']
        profile.kill_assists = data['kill_assists']
        profile.score_min = data['score_min']
        profile.quits = data['quits']
        profile.mcom_defend_kills = data['mcom_defend_kills']
        profile.mcom_destroyed = data['mcom_destroyed']
        profile.flags_captured_conquest = data['flags_captured_conquest']
        profile.flags_defended_conquest = data['flags_defended_conquest']
        profile.vehicles_destroyed = data['vehicles_destroyed']
        profile.vehicles_destroyed_assists = data['vehicles_destroyed_assists']
        profile.avg_weapon_accuracy = data['avg_weapon_accuracy']
        profile.longest_headshot = data['longest_headshot']
        profile.highest_kill_streak = data['highest_kill_streak']
        profile.skill = data['skill']
        profile.avenger_kills = data['avenger_kills']
        profile.savior_kills = data['savior_kills']
        profile.dogtags_taken = data['dogtags_taken']
        profile.flags_captured_ctf = data['flags_captured_ctf']
        profile.squad_score_bonus = data['squad_score_bonus']
        profile.repairs = data['repairs']
        profile.revives = data['revives']
        profile.heals = data['heals']
        profile.resupplies = data['resupplies']
        profile.shots_fired = data['shots_fired']
        profile.nemesis_kills = data['nemesis_kills']
        profile.highest_nemesis_streak = data['highest_nemesis_streak']
        profile.suppression_assists = data['suppression_assists']

        session.add(profile)
