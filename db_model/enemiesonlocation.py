from .base import Base
from sqlalchemy import Column, Integer, ForeignKey


class EnemiesOnLocation(Base):
	__tablename__ = 'EnemiesOnLocation'

	Id = Column(Integer, primary_key=True, nullable=False, unique=True)
	location_id = Column(Integer, ForeignKey('Location.Id'))
	enemi_id = Column(Integer, ForeignKey('Enemy.Id'))