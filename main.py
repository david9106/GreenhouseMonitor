import webapp2
import json
import cgi
import datetime
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
#from DataBase import Censado

#jsonToPython = json.loads(data)
#class Shout(db.Model):
#	message = db.StringProperty(required=True)
#	when = db.DateTimeProperty(auto_now_add=True)
class Censado(db.Model):
	id_LiSANDRA = db.StringProperty(required=True)
	type = db.StringProperty(required=True)
	value = db.StringProperty(required=True)
	#value = db.FloatProperty(required=True)
	when = db.DateTimeProperty(auto_now_add=True)

class Echo_parser(webapp2.RequestHandler):
	messg = 0
	def get(self):
		if Echo_parser.messg is not 0:
			self.response.write('Message received: ' + str(Echo_parser.messg))
			Echo_parser.messg = 0;
		else:
			self.response.write('Haven\'t heard about you... ' + str(Echo_parser.messg))

class Json_parser(webapp2.RequestHandler):
	def post(self):
		#jdata = json.loads(cgi.escape(self.request.body))
		#Echo_parser.messg = 1;
		#self.response.out.write(json.dumps(jdata))
		if self.request.get('busca'):
			#sensor = Censado.Censado(id_LiSANDRA = jdata['Id'], type = 'Centigrados', value = jdata['temperatura'])
			#sensor.put()
			sensor = Censado.all().filter('when >',datetime.datetime(2016,10,1)).filter('when <',datetime.datetime(2016,10,10)).filter('type =','Centigrados')
			sensor = Censado.all().filter('when <',datetime.datetime.now()).filter('type =','Centigrados')
			sensors = sensor.fetch(None)
			values={'sensors': sensors}
			self.response.out.write(template.render('data.html',values))


	def get(self):
		 self.response.out.write(template.render('data.html', {}))
		

app = webapp2.WSGIApplication([
    ('/', Json_parser),
], debug=True)