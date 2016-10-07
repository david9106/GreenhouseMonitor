import webapp2
import json
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template



#print "received message:", data

jsonData = '{"message": "Logan"}'
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
	
#def addToDB():

class MainPage(webapp2.RequestHandler):
     def get(self):    
		#self.response.out.write(template.render('index.html', {}))
		date_1='2016-09-25'
		date_2='2016-10-27'
		shouts = db.GqlQuery("SELECT * FROM Shout WHERE when <= :1",date_2) #si jala
		#shouts = db.GqlQuery("SELECT * FROM Shout WHERE when <= :1 AND when >= :2",date_2, date_1) #no jala :(
		values = {
			'shouts' : shouts
		}
		self.response.out.write(template.render('index.html',values))
		
     def post(self):
		#sens = Censado(grados=jsonToPython['temp'], luxes=jsonToPython['luz'], humedad=jsonToPython['hum'])
		sens = Shout(message=jsonToPython['message'])
		sens.put()
		self.redirect('/')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)