__author__ = 'jesuejunior'
from sqlalchemy import Integer, Column, String, Float
import core


class Profile(core.db.Model):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    url_profile = Column(String, nullable=False)
    url_weapons = Column(String, nullable=False)

    kills = Column(Integer)
    deaths = Column(Integer)
    kd_ratio = Column(Float)
    kill_assists = Column(Integer)
    score_min = Column(Integer)
    quits = Column(Integer)
    mcom_defend_kills = Column(Integer)
    mcom_destroyed = Column(Integer)
    flags_captured_conquest = Column(Integer)
    flags_defended_conquest = Column(Integer)

    vehicles_destroyed = Column(Integer)
    vehicles_destroyed_assists = Column(Integer)
    avg_weapon_accuracy  = Column(Float)
    longest_headshot = Column(Float)
    highest_kill_streak = Column(Integer)
    skill  = Column(Float)
    avenger_kills = Column(Float)
    savior_kills = Column(Integer)
    dogtags_taken = Column(Integer)
    flags_captured_ctf = Column(Integer)

    squad_score_bonus = Column(Float)
    repairs	= Column(Integer)
    revives	= Column(Integer)
    heals = Column(Integer)
    resupplies = Column(Integer)
    shots_fired = Column(Integer)
    highest_nemesis_streak = Column(Integer)
    nemesis_kills = Column(Integer)
    suppression_assists	= Column(Integer)