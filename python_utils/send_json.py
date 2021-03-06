import json
import urllib2
import sys #sys.argv
import ssl

def send_json_request(server_url, json_dict):
	"""send a json object by post request to a url and expects a json response"""
	try:
		req = urllib2.Request(server_url)
		req.add_header('Content-Type','application/json')
		#context = ssl._create_unverified_context()
		return urllib2.urlopen(req, json.dumps(json_dict))
	except ValueError as e:
		print("({!s})Error>> {!s}".format(send_json_request.__name__,e))	

def on_exit():
	"""Print that the program is over"""
	print('\nClosing program.')

if len(sys.argv) >= 2: #Checks if at least 2 params
	try:
		json_dict = {} #Initialize dictionary			
		
		for index in range(2,len(sys.argv)):#Iterates over the argument pairs, 2nd param is first value pair
			idN,valueN = sys.argv[index].split(":") #Get the pair components
			json_dict["{0}".format(idN)]="{0}".format(valueN) #Save the components in dict
				
		json_response = send_json_request(sys.argv[1], json_dict) #Send request 1st param is url
		print(json_response)
	except ValueError as e:
		print("({!s})Error>> {!s}".format(sys.argv[0],e))
	
else:
	print('\n>>Error\nNeed to provide at least 2 params.\n\nUsage: '+sys.argv[0]+' <server_url> <id1:value1> [,<id2:value2>...<idN:valueN>]\n\n')
