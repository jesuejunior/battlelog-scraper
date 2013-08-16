from alchemytools.context import managed
from core.db import Session
from core.db.profile import Profile
from core.db.stats import Stats

__author__ = 'jesuejunior'

def create(data):

    with managed(Session) as session:
        profile = session.query(Profile).filter_by(username=data['username']).all()
    if profile:
        return False
    else:
        with managed(Session) as session:
            profile = Profile(username=data['username'], url_stats=data['url_stats'], url_weapons=data['url_weapons'], url_vehicles=data['url_vehicles'] )
            session.add(profile)
        return True

def updater(data):
    with managed(Session) as session:
        stats = session.query(Stats).join(Profile).filter(Profile.username==data['username']).first()
        if not stats:
            stats = Stats()
            profile = session.query(Profile).filter_by(username=data['username']).all()[0]
            profile.stats = stats
            session.add(profile)

        stats.level = data['level']
        stats.score_assault = data['score_assault']
        stats.score_engineer = data['score_engineer']
        stats.score_support = data['score_support']
        stats.score_recon = data['score_recon']
        stats.score_vehicles = data['score_vehicles']
        stats.score_combat = data['score_combat']
        stats.score_award = data['score_award']
        stats.score_unlocks = data['score_unlocks']
        stats.score_total = data['score_total']

        stats.kills = data['kills']
        stats.deaths = data['deaths']
        stats.kd_ratio = data['kd_ratio']
        stats.kill_assists = data['kill_assists']
        stats.score_min = data['score_min']
        stats.quits = data['quits']
        stats.mcom_defend_kills = data['mcom_defend_kills']
        stats.mcom_destroyed = data['mcom_destroyed']
        stats.flags_captured_conquest = data['flags_captured_conquest']
        stats.flags_defended_conquest = data['flags_defended_conquest']

        stats.vehicles_destroyed = data['vehicles_destroyed']
        stats.vehicles_destroyed_assists = data['vehicles_destroyed_assists']
        stats.avg_weapon_accuracy = data['avg_weapon_accuracy']
        stats.longest_headshot = data['longest_headshot']
        stats.highest_kill_streak = data['highest_kill_streak']
        stats.skill = data['skill']
        stats.avenger_kills = data['avenger_kills']
        stats.savior_kills = data['savior_kills']
        stats.dogtags_taken = data['dogtags_taken']
        stats.flags_captured_ctf = data['flags_captured_ctf']

        stats.squad_score_bonus = data['squad_score_bonus']
        stats.repairs = data['repairs']
        stats.revives = data['revives']
        stats.heals = data['heals']
        stats.resupplies = data['resupplies']
        stats.shots_fired = data['shots_fired']
        stats.nemesis_kills = data['nemesis_kills']
        stats.highest_nemesis_streak = data['highest_nemesis_streak']
        stats.suppression_assists = data['suppression_assists']

        session.add(stats)
