from sqlalchemy.orm import relationship

__author__ = 'jesuejunior'
from sqlalchemy import Integer, Column, String, Float, ForeignKey
import core


class Profile(core.db.Model):
    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    url_stats = Column(String, nullable=False)
    url_weapons = Column(String, nullable=False)
    url_vehicles = Column(String, nullable=False)

    stats = relationship("Stats", uselist=False, backref="profile")

