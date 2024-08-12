from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class BaseModel(Base):
	__abstract__ = True

	Id = Column(Integer, nullable=False, unique=True, primary_key=True)
	created_at = Column(DateTime, nullable=False, default=datetime.now)
	updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return f'<{self.__class__.__name__}(id={self.Id!r})>'

class IncrementBaseModel(Base):
	__abstract__ = True

	Id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincremnet=True)
	created_at = Column(DateTime, nullable=False, default=datetime.now)
	updated_at = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

	def __repr__(self):
		return f'<{self.__class__.__name__}(id={self.Id!r})>'