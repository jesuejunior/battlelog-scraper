from sqlalchemy.orm import relationship

__author__ = 'jesuejunior'
from sqlalchemy import Integer, Column, String, Float, ForeignKey
import core


class Stats(core.db.Model):
    __tablename__ = 'stats'

    id = Column(Integer, primary_key=True)
    profile_id = Column(Integer, ForeignKey('profile.id'))

    level = Column(Integer, default=0)
    score_assault = Column(Integer, default=0)
    score_engineer = Column(Integer, default=0)
    score_support = Column(Integer, default=0)
    score_recon = Column(Integer, default=0)
    score_vehicles = Column(Integer, default=0)
    score_combat = Column(Integer, default=0)
    score_award = Column(Integer, default=0)
    score_unlocks = Column(Integer, default=0)
    score_total = Column(Integer, default=0)

    kills = Column(Integer, default=0)
    deaths = Column(Integer, default=0)
    kd_ratio = Column(Float, default=0.0)
    kill_assists = Column(Integer, default=0)
    score_min = Column(Integer, default=0)
    quits = Column(Integer, default=0)
    mcom_defend_kills = Column(Integer, default=0)
    mcom_destroyed = Column(Integer, default=0)
    flags_captured_conquest = Column(Integer, default=0)
    flags_defended_conquest = Column(Integer, default=0)

    vehicles_destroyed = Column(Integer, default=0)
    vehicles_destroyed_assists = Column(Integer, default=0)
    avg_weapon_accuracy  = Column(Float, default=0.0)
    longest_headshot = Column(Float, default=0.0)
    highest_kill_streak = Column(Integer, default=0)
    skill  = Column(Float, default=0.0)
    avenger_kills = Column(Float, default=0.0)
    savior_kills = Column(Integer, default=0)
    dogtags_taken = Column(Integer, default=0)
    flags_captured_ctf = Column(Integer, default=0)

    squad_score_bonus = Column(Float, default=0.0)
    repairs	= Column(Integer, default=0)
    revives	= Column(Integer, default=0)
    heals = Column(Integer, default=0)
    resupplies = Column(Integer, default=0)
    shots_fired = Column(Integer, default=0)
    highest_nemesis_streak = Column(Integer, default=0)
    nemesis_kills = Column(Integer, default=0)
    suppression_assists	= Column(Integer, default=0)