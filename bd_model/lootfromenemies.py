from .base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LootFromEnemies(Base):
	__tablename__ = 'LootFromEnemies'


	Id = Column(Integer, primary_key=True, nullable=False, unique=True)
	enemi_Id = Column(Integer, ForeignKey('Enemy.Id'))
	trophy_Id = Column(Integer, ForeignKey('PlayerItem.Id'))
