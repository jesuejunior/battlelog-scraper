__author__ = 'jesuejunior'

class Weapons(battle.db.Model):
    __tablename__ = 'directory'

    id = Column(Integer, primary_key=True)
    base = Column(String, nullable=False)
    index_file = Column(String, nullable=False)
    default_ctype = Column(String, nullable=False)
    cache_ttl = Column(Boolean, default=0)
