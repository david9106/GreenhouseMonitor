import requests
import json
import time

url = "http://192.168.0.106/getjson/catchJson.php"
#url = "https://sensado-invernadero.appspot.com/set_sensors"
#url = "https://redsensoreslisandra.appspot.com"
headers = {'Content-type':'application/json'}

def send(lista_sensores):
        for sensor in lista_sensores:
                sendJson(sensor)
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
