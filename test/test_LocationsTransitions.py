import unittest
from io import StringIO
import sys
import unittest.mock
import logging
from db_model import User, create_session, Location, LocationTransitions as LocTs
from db_model.base import Base


class event:
	text = 'start'
	user_id = '1'

class LocationTransitions(unittest.TestCase):

	def test_meta_rest(self):
		log = logging.getLogger('test')
		try:
			new_user = User(Id=20, location_id=0)
			session = create_session()
			session.add(new_user)
			session.commit()
			session.close()
		except BaseException as err:
			log.error(err, exc_info=True)

	def test_location(self):
		from_ = Location(name='1')
		new_data = [
			from_,
			Location(name='2'),
			Location(name='3'),
			LocTs(locationIdFrom=1, locationIdTo=2),
			LocTs(locationIdFrom=1, locationIdTo=3)
		]
		session = create_session()
		session.add_all(new_data)
		session.commit()
		query = from_.get_transitions(session)
		logging.warning(query)
		logging.warning(query.all())
