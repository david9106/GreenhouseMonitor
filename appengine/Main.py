import webapp2
from Handlers import Parser,MainPage
							
app = webapp2.WSGIApplication([
    ('/set_sensors',Parser.Json_parser),
    ('/get_csv', MainPage.CSV_provider),
    ('/', MainPage.Graph_display)
], debug=False)


def main():
	app.run()
	
if __name__ == '__main__':
    main()
