from .base import IncrementBaseModel
from sqlalchemy import Column, Integer, String, Text, ForeignKey, relationship


class PlayerItem(IncrementBaseModel):
	__tablename__ = 'PlayerItem'

	name = Column(String(20), unique=True, nullable=False)
	description = Column(Text)
	i_type = Column(String(20), nullable=False)
	action = Column(String(20), nullable=False)
	item_value = Column(SmallInteger, nullable=False)
	iamge_id = Column(Integer, ForeignKey('Attachments.Id'))
	image = relationship('Attachments', uselist=False)
	price = Column(Integer, nullable=False)
