import webapp2
from Handlers import Parser
							
app = webapp2.WSGIApplication([
    ('/set_sensors',Parser.Json_parser),
    ('/echo', Parser.Echo_parser)
], debug=False)


def main():
	app.run()
	
if __name__ == '__main__':
    main()
