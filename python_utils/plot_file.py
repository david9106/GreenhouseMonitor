#!/usr/bin/python3.4m
#***** Plot the values read from a file 
#	It can plot 3 temp/hum sensors of the sensors.
#	Start graphing always from 0 seconds	
#	Different colors:
#		2 - Blue
#		3 - Green
#		4 - Red
#	
#
#	by Rafael Karosuo rafaelkarosuo@gmail.com
#
#
#	The sequence is:
#		sensor_id, time, value1, value2
#	
#	sensor_id is the port number where it is connected
#	time is the seconds passed since the start of reading time, which is 0
#	value1 (a/o value2) are the sensor values measured, value2 applies to the sensors like DHT22 or others that come with 2 values


import sys #argv
import os #open files
import matplotlib.pyplot as plt
import datetime #to_datetime function

##It serves as a reference, it'll enable that no matter when the values where taken
# always will start graph from zero seconds
first_time = '' #Global first time

def to_datetime(time):
	"""Converts a string amount of seconds, to datetime object"""
	time = int(time) #Parse it to int
	my_date = datetime.datetime.fromtimestamp(time) #gets epoch time + seconds
	ref_date = datetime.datetime.fromtimestamp(0) #gets epoch time as ref
	diff_time = my_date - ref_date #Gets the time diff, means seconds passed in format h:mm:ss
	return datetime.datetime.strptime(str(diff_time),"%H:%M:%S") #Parses diff_time to datetime

def to_timedelta_string(time):
	"""Converts a string amount of seconds, to a formatted string h:mm:ss"""
	time = int(time) #Parse it to int
	my_date = datetime.datetime.fromtimestamp(time) #gets epoch time + seconds
	ref_date = datetime.datetime.fromtimestamp(0) #gets epoch time as ref
	diff_time = my_date - ref_date #Gets the time diff, means seconds passed in format h:mm:ss
	hours,minutes,seconds = str(diff_time).split(":") ##Get components
	return '{:0>1}:{:0>2}:{:0>2}'.format(hours,minutes,seconds)
	
	
def set_first_time(the_file):
	try:
		sensor_id,time,hum,temp,erro_code = the_file.readline().split(",")
		global first_time
		first_time = time
	except ValueError as e:
		print("Error finding first time: {0}".format(e))	


def rt_plot(values):	
	"""Plots data of the sensor saved"""
	plt.ion() #interactive mode on	
	plt.legend(loc="upper center") #Position of the labels
	try:		
		sensor_id,time,hum,temp,error_code = values.split(",")	
		print(to_timedelta_string(int(time) - int(first_time)))
		###Arbitrary calibrations 
		if sensor_id == '3':
			hum = str(float(hum)+70.0)
		if sensor_id == '2':
			hum = str(float(hum)-9.0)
		#if sensor_id == '4':
			#hum = str(float(hum)-9.0)
		
		temp = str(float(temp)-1.0)
		
		xaxis_lval = int(int(time)/100) * 100; #Define the lower value on X axis
		xaxis_hval = xaxis_lval + 100; #Define the higher value on X axis, both has a 100pts gap

		plt.figure(1) #Select window
		plt.subplot(211)
		plt.axis([xaxis_lval,xaxis_hval,50,100])			
		plt.ylabel('Hum %RH')			
		#plt.plot(time, hum,'bo-')
		plt.legend("234") #Paint sensor type with color associated
		if sensor_id == '2':
			plt.plot(time, hum,'bo-')
		elif sensor_id == '3':
			plt.plot(time, hum,'go-')
		else:
			plt.plot(time, hum,'ro-')

		plt.title("Bakin box sensors") #Window title
		plt.subplot(212)
		plt.legend("234") #Paint sensor type with color associated
		plt.grid(True) #Paint the grid lines
		plt.axis([xaxis_lval,xaxis_hval,20,30])				
		plt.ylabel('Temp C')	
		#plt.plot(time, temp,'ro-')
		
		if sensor_id == '2':
			plt.plot(time, temp,'bo-')
		elif sensor_id == '3':
			plt.plot(time, temp,'go-')
		else:
			plt.plot(time, temp,'ro-')
			
		plt.pause(0.0005)		
		plt.show()
	except ValueError:
		print('\n>>Error\nMust be more than one value to unpack')

def on_exit():
	"""Present message of exiting program"""
	print("Closing program...")
	
try:
	if len(sys.argv) > 1: #Check if file name is given
		f = None; #File Objects

		try:
			f = open(sys.argv[1]) #Open for read
			set_first_time(f) #Sets the ref time
			file_content = f.read() #Read entire file to speed up graphing
			file_content = file_content.split("\n") #Get a list with the file lines
			for line in file_content: #Iterate on each line
				if line: #Ignore blank lines
					rt_plot(line) #plot saved values
		except IOError as e:
			print "\n>>Error\nI/O error({0}): {1}".format(e.errno, e.strerror) #Mainly if no file with given name exists		
				
		#for line in f: #Iterate over all file lines
			#if line and line != '\n': #Ignore blank and intro only lines
				#rt_plot(line) #plot saved values
	else:
		print('\n>>Error\nNeed to provide at least 1 param.\n\nUsage: '+sys.argv[0]+' <file_name>\n\n')
except KeyboardInterrupt:
	on_exit()
