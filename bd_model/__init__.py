from sqlalchemy import create_engine, MetaData
import atexit


engine = create_engine('sqllite://bases/test_db.db')
metaData = MetaData()
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


def close_database():
	engine.dispose()
