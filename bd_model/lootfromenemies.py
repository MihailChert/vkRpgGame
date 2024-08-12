from .base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LootFromEnemies(Base):
	__tablename__ = 'LootFromEnemies'

	enemi_Id = Column(Integer, ForeignKey('Enemi.Id'))
	trophy_Id = Column(Integer, ForeignKey('PlayerItem.Id'))
