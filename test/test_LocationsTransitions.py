import unittest
from io import StringIO
import sys
import unittest.mock
import logging
from db_model import User, create_session, Location, LocationTransitions as LocTs
from db_model.base import Base
import pdb


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
			user = session.query(User.Id).filter(User.Id == 20).one()
			# pdb.set_trace()
		except BaseException as err:
			log.error(err, exc_info=True)

		finally:
			session.commit()
			session.close()
		self.assertEqual(user[0], 20)

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
		logging.debug(query)
		ansver = [2, 3]
		for i in query.all():
			self.assertTrue(i.Id in ansver)
		logging.debug(query.all())
