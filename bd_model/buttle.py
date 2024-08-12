from .base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Buttle(Base):
	__tablename__ = 'Buttle'

	Id = Column(Integer, nullable=False, unique=True, primary_key=True)
	path_to_session = Column(String(50), nullable=False)
	group_id = Column(Integer, ForeignKey('Group.Id'))
	group = relationship('Group')
