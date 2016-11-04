import webapp2
from Handlers import Parser,MainPage
							
app = webapp2.WSGIApplication([
    ('/set_sensors',Parser.JSON_parser),
    ('/get_csv', MainPage.CSV_provider),
    ('/get_json', MainPage.JSON_provider),
    ('/get_config', MainPage.Config_provider),
<<<<<<< HEAD
	('/save_config',MainPage.Phone_Config),
    ('/print_html',MainPage.MainPageHandler)
||||||| merged common ancestors
	('/save_config',MainPage.Phone_Config)
=======
	('/save_config',MainPage.Data_Config),
>>>>>>> d81be87a71dc20b462fefa24580ff953fa85e099
], debug=False)

def main():
	app.run()
	
if __name__ == '__main__':
    main()
