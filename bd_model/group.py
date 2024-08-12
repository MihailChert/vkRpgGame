from .base import Base
from sqlalchemy import Column, Integer, Enum, String, ForeignKey, relationship
from enum import IntEnum, auto


class GroupType(IntEnum):
	buttle = auto()
	guild = auto()



class Group(IncrementBaseModel):
	__tablename__ = 'Group'

	Id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
	name = Column(String(20))
	g_type = Column(Enum(GroupType), nullable=False, default=GroupType.buttle)
	buttle = relationship('Buttle', uselist=False)
	partyInt = Column(Integer, nullable=False, ForeignKey('User.Id'))
