import webapp2
import json
import cgi		


class Json_parser(webapp2.RequestHandler):
	def post(self):
		jdata = json.loads(cgi.escape(self.request.body))
		Echo_parser.messg = 1;
		#self.redirect('/echo');
		#jmessage = {'message':'Hello, what are you doing here?'}
		self.response.write(json.dumps(jdata))
	def get(self):
		self.response.write('Hello, what are you doing here?')
