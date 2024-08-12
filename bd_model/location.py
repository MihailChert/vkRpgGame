from .base import IncrementBaseModel
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, relationship


class Location(IncrementBaseModel):
	__tablename__ = 'Location'

	descriptions = Column(Text)
	lastTimeEvent = Column(DateTime)
	name = Column(String(40), nullable=False, unique=True)
	iamge_id = Column(Integer, ForeignKey('Attachments.Id'))
	image = relationship('Attachments', uselist=False)
	enemies = relationship('Enemy', secondary='EnemiesOnLocation')
	transition = relationship('Location', secondary='LocationsTransitions')
	event_count = Column(SmallInteger, default=0)
	event_brak = Column(Interval)
	max_event_count = Column(SmallInteger)
	players = relationship('User')
