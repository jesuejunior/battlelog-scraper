__author__ = 'jesuejunior'

from sqlalchemy import Integer, Column, Boolean, String
import core


class Weapons(core.db.Model):
    __tablename__ = 'weapons'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    kills = Column(Integer, nullable=False)
    accurary = Column(Integer, nullable=False)
    service_star = Column(Boolean, default=0)
