import requests
import json

#Usar la ip correspondiente
url = "http://192.168.1.74/getjson/catchJson.php"
##url = "https://sensado-invernadero.appspot.com/set_sensors"
headers = {'Content-type':'application/json'}
def sendJson(sensores):
	#Se envia la informacion de los sensores al servidor
	response = requests.post(url,json.dumps(sensores),timeout=5)
	#Nota: Esta parte es solo para impresion
	if response.status_code == 200:
		data = response.json()
		#Se muestra lo recibido por el servidor
		print ("Servidor:")
		d = json.loads(data)
		print (d['temperatura'])
		print (d['humedad'])
		print (d['luz'])
		print (d['CO2'])
		print (d['fecha'])
		print (d['hora'])
	else:
		print ("Hubo un error en la conexion")
        
