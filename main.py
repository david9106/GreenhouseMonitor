import webapp2
import socket
import json
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template



#print "received message:", data

jsonData = '{"message": "Lile"}'
jsonToPython = json.loads(jsonData)
#jsonToPython = json.loads(data)

class Censado(db.Model):
	grados = db.FloatProperty(required=True)
	luxes = db.FloatProperty(required=True)
	humedad = db.FloatProperty(required=True)
	when = db.DateTimeProperty(auto_now_add=True)

class Shout(db.Model):
	message = db.StringProperty(required=True)
	when = db.DateTimeProperty(auto_now_add=True)
	
def addToDB():

class MainPage(webapp2.RequestHandler):
     def get(self):    
		self.response.out.write(template.render('index.html', {}))
     def post(self):
		#sens = Censado(grados=jsonToPython['temp'], luxes=jsonToPython['luz'], humedad=jsonToPython['hum'])
		sens = Shout(message=jsonToPython['message'])
		sens.put()
		self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)