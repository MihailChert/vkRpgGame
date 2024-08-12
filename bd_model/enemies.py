from .base import IncrementBaseModel
from sqlalchemy import Column, Integer, String, ForeignKey, relationsip, Text

class Enemy(IncrementBaseModel):
	__tablename__ = 'Enemy'

	name = Column(String(45), nullable=False, unique=True)
	health = Column(Integer, nullable=False)
	resistence = Column(Text)
	image = Column(Integer, ForeignKey('Attachments.Id'))
	damage = Column(Integer, nullable=False)
	loot = relationsip('LootFromEnemies')
	locations = relationsip('EnemiesOnLocation')
