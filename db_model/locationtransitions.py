from .base import Base
from sqlalchemy import Column, Integer, ForeignKey


class LocationTransitions(Base):
	__tablename__ = 'LocationsTransitions'


	Id = Column(Integer, primary_key=True, nullable=False, unique=True)
	locationIdFrom = Column(Integer, nullable=False)
	locationIdTo = Column(Integer, nullable=False)
