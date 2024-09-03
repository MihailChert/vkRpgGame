from sqlalchemy import create_engine
import atexit
from sqlalchemy.orm import Session, sessionmaker
import os

engine = create_engine(os.environ['db_config_path'])
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
from .enemiesonlocation import EnemiesOnLocation


def create_all():
	from .base import Base
	Base.metadata.create_all(engine)

def create_session():
	return Session(bind=engine)



create_all()
