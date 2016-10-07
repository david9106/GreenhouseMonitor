import webapp2
import json
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template



#print "received message:", data

jsonData = '{"message": "Rigan"}'
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
		date_1='2016-09-01'
		date_2='2016-10-06'
		time_1 = '22:00:00'
		time_2 = '23:00:00'
		
		shouts = db.GqlQuery("SELECT * FROM Shout WHERE when < DATETIME('2016-10-06 22:30:03') AND when > DATETIME('2016-09-06 22:30:03')",date_1, time_1, date_1, time_2)#,time_1,time_2 ) #si jala
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