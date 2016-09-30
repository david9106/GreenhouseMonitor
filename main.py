import webapp2
import json
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

j = '{"message": "hell"}' 

class Censado(db.Model):
	grados = db.FloatProperty(required=True)
	luxes = db.FloatProperty(required=True)
	humedad = db.FloatProperty(required=True)
	when = db.DateTimeProperty(auto_now_add=True)

class Shout(db.Model):
	message = db.StringProperty(required=True)
	when = db.DateTimeProperty(auto_now_add=True)

class MainPage(webapp2.RequestHandler):
     def get(self):    
		self.response.out.write(template.render('index.html', {}))
     def post(self):
		shout = Shout( message=self.request.get('message'))
		#shout = Shout(message=self.request.get(json.loads(j))
		shout.put()
		self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)