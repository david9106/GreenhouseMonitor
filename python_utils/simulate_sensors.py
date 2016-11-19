#
#	Simulate sensor reading over cerain amount of time
#
#	The sensor json package, is the used on the greenhouse monitoring system
#	{"Tipo":sensor_type, "Valor":measured_value, "Ubicacion":id_lisandra}
#
#	by Rafael Karosuo, rafaelkarosuo@gmail.com

#import json
import send_json #send_json_to_server function
from time import sleep
import random
import sys #cmd params

if len(sys.argv) == 3: #Checks if at least 2 params
	try:
		while True:
			try:				
				json_dict = {} #Initialize dictionary					
				sensor_types = ["CO2","Temperatura","Humedad","Iluminacion"] #Available sensor_types
				id_lisandras = [10,15,20,25,30,35,40] #Lisandras available
				json_dict["Tipo"] = str(random.choice(sensor_types)) #Selects a sensor_type randomly
				
				#Depending on sensor type, put limits and generate random measure
				
				if json_dict["Tipo"] == "C02":
					json_dict["Valor"] = str(round(random.randint(350,450) + random.random(),2)) #Randomly generates a measure, bt 350-450 ppm with 2 decimals
					
				elif json_dict["Tipo"] == "Temperatura":
					json_dict["Valor"] = str(round(random.randint(25,38) + random.random(),2)) #Randomly generates a measure, bt 25-35 C with 2 decimals
					
				elif json_dict["Tipo"] == "Humedad":
					json_dict["Valor"] = str(round(random.randint(50,100) + random.random(),1)) #Randomly generates a measure, bt 50-100 %RH with 1 decimal
					
				else: #sensor_types == "Iluminacion":
					#1k luxes near windows at clear day
					#10k luxes outside on that same day
					json_dict["Valor"] = str(round(random.randint(1000,10000) + random.random(),2)) #Randomly generates a measure, bt 1000-10000 luxes with 2 decimals
					
				json_dict["Ubicacion"] = str(random.choice(id_lisandras))
				json_response = send_json.send_json_request(sys.argv[1],json_dict) #Uses the url, 1st param
				
				print(json_response) #Prints what server answered
				sleep(float(sys.argv[2])) #Uses the 2nd param, the resend time interval
						
			except ValueError as e:
				print("({!s})Error>>{!s}".format(sys.argv[0],e))
	except KeyboardInterrupt:
		print("Ending simulation...\nClosing program...")
else:
	print('\n>>Error\nNeed to provide 2 params.\n\nUsage: '+sys.argv[0]+' <server_url> <resend_time_interva>\n\n<resend_time_interva> In seconds, could be float\n\n')

