import xml.dom.minidom
import pdb
import os


file = os.path.join(os.path.dirname(__file__), '../bot_view/messages_start.xml')

doc = xml.dom.minidom.parse(file)

pdb.set_trace()