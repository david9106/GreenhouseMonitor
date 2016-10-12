import webapp2

class Graph_display(webapp2.RequestHandler):
	#GraphicsHandler.update_csv();


class CSV_provider(webapp2.RequestHandler):
	def get(self):
		self.response.out.write('''<html><body><p>'''+ self.request.get("sensor_type") +'''</p></body></html>''')
	#this_year_measures = BDHandler.get_this_year_measures("Temperatura")
	
