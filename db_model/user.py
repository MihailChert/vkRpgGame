from .base import BaseModel
from sqlalchemy import Column, Integer, String, Text, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship


class User(BaseModel):
	__tablename__ = 'User'

	location_id = Column(Integer, ForeignKey('Location.Id'))
	location = relationship('Location', uselist=False)
	items = Column(Text)
	health = Column(SmallInteger, nullable=False, default=100)
	role = Column(String(20), nullable=False, default='beginer')
	effect_status = Column(String(40))
	max_health = Column(Integer, nullable=False, default=100)
	last_command = Column(String(45))
	group = relationship('Group')
