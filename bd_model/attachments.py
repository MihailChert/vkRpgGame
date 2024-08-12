from .base import IncrementBaseModel
from sqlalchemy import Column, String


class Attachments(IncrementBaseModel):
	__tablename__ = 'Attachments'

	mm_type = Column(String(10), nullable=False)
	path = Column(String(50), nullable=False)
