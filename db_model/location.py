from .base import IncrementBaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, SmallInteger, Interval
from sqlalchemy.orm import relationship


class Location(IncrementBaseModel):
	__tablename__ = 'Location'

	descriptions = Column(Text)
	lastTimeEvent = Column(DateTime)
	name = Column(String(40), nullable=False, unique=True)
	iamge_id = Column(Integer, ForeignKey('Attachments.Id'))
	image = relationship('Attachments', uselist=False)
	enemies = relationship('Enemy', secondary='EnemiesOnLocation')
	# transition = relationship('LocationsTransitions')
	event_count = Column(SmallInteger, default=0)
	event_brak = Column(Interval)
	max_event_count = Column(SmallInteger)
	players = relationship('User', viewonly=True)

	def get_transitions(self, session):
		transitions = Base.registry._class_registry['LocationTransitions']
		query = session.query(Location).join(
				transitions,
				transitions.locationIdTo == Location.Id
			).filter(transitions.locationIdFrom == self.Id)
		return query

	def get_transition_names(self, session):
		transitions = Base.registry._class_registry['LocationTransitions']
		query = session.query(Location.name).join(
				transitions,
				transitions.locationIdTo == Location.Id
			).filter(transitions.locationIdFrom == self.Id)
		return query

	@classmethod
	def get_transitions_cls(cls, session, from_id):
		transitions = Base.registry._class_registry['LocationTrnasitions']
		query = session.query(Location).join(
				transitions,
				transitions.locationIdTo == Location.Id
			).filter(transitions.locationIdFrom == from_id)
		return query

	@classmethod
	def get_transition_names_cls(cls, session, from_id):
		transitions = Base.registry._class_registry['LocationTransitions']
		query = session.query(Location.name).join(
				transitions,
				transitions.locationIdTo == Location.Id
			).filter(transitions.locationIdFrom == from_id)
		return query
