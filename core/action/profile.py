from alchemytools.context import managed
from core.db import Session
from core.db.profile import Profile

__author__ = 'jesuejunior'

def profile_create(data):

    with managed(Session) as session:
        profile = session.query(Profile).filter_by(username=data['username']).all()
    if profile:
        return False
    else:
        with managed(Session) as session:
            profile = Profile(username=data['username'], url_stats=data['url_stats'], url_weapons=data['url_weapons'], url_vehicles=data['url_vehicles'] )
            session.add(profile)
        return True
