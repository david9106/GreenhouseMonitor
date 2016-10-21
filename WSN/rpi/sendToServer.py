import requests
import json
import time
import urllib2
import ssl

url = "http://192.168.0.106/getjson/catchJson.php"
url2 = "https://sensado-invernadero.appspot.com/get_alert_config"
#url = "https://sensado-invernadero.appspot.com/set_sensors"
#url = "https://redsensoreslisandra.appspot.com"
headers = {'Content-type':'application/json'}

def send(lista_sensores):
        for sensor in lista_sensores:
                sendJson(sensor,url)
                time.sleep(1)
                
def sendJson(sensor):
        j=json.dumps(sensor)
        try:
                #Se envia la informacion de los sensores al servidor
                print("json: "+j)
                response = requests.post(url,j,timeout=1)
                print("Server response code: "+str(response.status_code))                
                if response.status_code == 200:
                        print ("Enviado ...")
                else:
                        print ("Hubo un error en la conexion")
        except requests.exceptions.Timeout:
                print("Timeout ...")
        except requests.exceptions.TooManyRedirects:
                print("Demasiadas redirecciones ...")
        except requests.exceptions.RequestException as e:
                print(e)
                sys.exit(1)
                
def send_json_request(server_url, json_dict):
      	"""send a json object by post request to a url and expects a json response"""
      	req = urllib2.Request(server_url)
       	req.add_header('Content-Type','application/json')
       	context = ssl._create_unverified_context()
      	response = urllib2.urlopen(req, json.dumps(json_dict), context=context)      	
      	#response = requests.post(server_url,json_dict,timeout=1)
        return json.load(response) 
       
def getconfig(comand): 
#Checks if at least 2 params

  json_dict = {} #Initialize dictionary	
  #Iterates over the argument pairs, 2nd param is first value pair
  idN,valueN = comand.split(":") #Get the pair components
  json_dict["{0}".format(idN)]="{0}".format(valueN) #Save the components in dict
  #sendJson(json_dict,url2)		
  json_response = send_json_request(url2, json_dict) #Send request 1st param is url
  return json_response

		
