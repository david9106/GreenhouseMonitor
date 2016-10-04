import webapp2
import json
import cgi

sensor_data = None

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
		jdata = json.loads(cgi.escape(self.request.body))
		Echo_parser.messg = 1;
		#self.redirect('/echo');
		#jmessage = {'message':'Hello, what are you doing here?'}
		self.response.write(json.dumps(jdata))
	def get(self):
		self.response.write('Hello, what are you doing here?')
