import webapp2
from Handlers import Parser,MainPage
							
app = webapp2.WSGIApplication([
    ('/set_sensors',Parser.JSON_sensor_parser),
    ('/get_csv', MainPage.CSV_provider),
    ('/get_json', MainPage.JSON_provider),
    ('/get_config', MainPage.Config_provider),
	('/save_config',MainPage.Data_Config),
], debug=False)

def main():
	app.run()
	
if __name__ == '__main__':
    main()
