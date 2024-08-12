from sqlalchemy import create_engine
import atexit
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine('sqlite:///bd_model/bases/test_db.db')
def close_database():
	engine.dispose()
atexit.register(close_database)

from .user import User
from .attachments import Attachments
from .buttle import Buttle
from .enemies import Enemy
from .group import Group
from .location import Location
from .locationtransitions import LocationTransitions
from .lootfromenemies import LootFromEnemies
from .playeritems import PlayerItem


def create_all():
	from .base import Base
	Base.metadata.create_all(engine)

def create_session():
	return sessionmaker(bind=engine)



create_all()
