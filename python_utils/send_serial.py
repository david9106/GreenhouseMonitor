#!/usr/bin/python3.4m
#***** Send the values read from SERIAL port to server, the server is a replica of the greenhouse monitoring
#	It can plot multiple entries of the sensors (server do it)
#	It can log the values on to a file
#	It can just plot without log (just send to server without saving on file)
#
#	by Rafael Karosuo rafaelkarosuo@gmail.com
#
#
#	The sequence is:
#		sensor_id, time, value1 , value2
#	
#	sensor_id is the port number where it is connected
#	time is the seconds passed since the start of reading time, which is 0
#	value1 and value2 are the sensor values measured, temp and hum.


import serial #serial
import sys #argv
import os #open files
import json #json dumps
import urllib2 #POST request
from time import sleep #sleep in seconds

server_parser_url = 'http://localhost:8080/set_sensors'
#server_parser_url = 'https://sensado-invernadero.appspot.com/set_sensors'

def send_to_server(values):	
	"""Send's a JSON object of the sensor measured to the server as POST req."""
	try:
		
		#split string on variables
		sensor_id,time,hum,temp,error_code = values.split(",")
		
		##Setup the request
		req = urllib2.Request(server_parser_url)
		req.add_header('Content-Type','application/json')
		
		##Prepare first object
		tmp_dict = {}
		tmp_dict["Tipo"] = "Humedad"
		tmp_dict["Valor"] = hum
		tmp_dict["Ubicacion"] = sensor_id
		
		#Sends the first object, with Humidity
		response = urllib2.urlopen(req, json.dumps(tmp_dict)) 
		response_data = json.load(response)
		print response_data
		
		##Prepare second object
		tmp_dict["Tipo"] = "Temperatura"
		tmp_dict["Valor"] = temp
		tmp_dict["Ubicacion"] = sensor_id
		
		#Sends the second object, with Temperature
		req2 = urllib2.Request(server_parser_url)
		req2.add_header('Content-Type','application/json')
		response2 = urllib2.urlopen(req2, json.dumps(tmp_dict)) 
		response_data = json.load(response2)
		print response_data
		
	except ValueError:
		print('\n>>Error\nMust be more than one value to unpack')

def on_exit():
	"""Print that it's over and closes the port"""
	print('\nEnd measuring.')
	print('Closing port...')
	serial_port.close()

try:
	if len(sys.argv) >= 3:
		serial_port = None;
		f = None;
		try:
			baud_speed = int(sys.argv[2])
			serial_port = serial.Serial(sys.argv[1],baud_speed,timeout=2)
		except ValueError:
			print('\n>>Error\nBaud speed needs to be an integer value\n\n')

		if len(sys.argv) == 4:
			try:
				f = open(sys.argv[3],'a',os.O_NONBLOCK);
			except IOError as e:
				print "\n>>Error\nI/O error({0}): {1}".format(e.errno, e.strerror)
		
		while True:
			values = serial_port.readline() #Read the sequence of values
			if f is not None:
				f.write(values); #Log on to file
				f.write('\n')
				f.flush()
			#print(values)
			send_to_server(values)
			#sleep(120) ##Sleep 2 mins
		
	else:
		print('\n>>Error\nNeed to provide at least 2 params.\n\nUsage: '+sys.argv[0]+' <port name> <baud speed> [<log file name>]\n\n')
except KeyboardInterrupt:
	on_exit()
