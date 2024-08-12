from .base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LocationTransitions(Base):
	__tablename__ = 'LocationsTransitions'

	locationIdFrom = Column(Integer, ForeignKey('Location.Id'))
	locationIdTo = Column(Integer, ForeignKey('Location.Id'))
