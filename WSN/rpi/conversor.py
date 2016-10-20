import math

#funcion encargada dee ajustar las mediciones a su valor segun la hoja de especificaciones
def ajustarMediciones(lista_sensores):
        for sensor in lista_sensores:
                ajustar(sensor)


def ajustar(sensor):
        if sensor['Tipo']=='temperatura':
                d1 = -39.6
                d2 = 0.01
                sensor['Valor']= d1+d2*sensor['Valor']
                sensor['Valor'] =format(sensor['Valor'],'.2f')
                 
        if sensor['Tipo']=='humedad':
                c1 = -2.0468
                c2 = 0.0367
                c3 = -1.5955e-6
                sensor['Valor'] = c1 + c2 * sensor['Valor'] + c3 * math.pow(sensor['Valor'],2)
                sensor['Valor'] =format(sensor['Valor'],'.2f')
                
        if sensor['Tipo']=='luz':
                sensor['Valor'] = math.exp(3.3/(1024 * 0.56))*sensor['Valor']
                sensor['Valor'] =format(sensor['Valor'],'.2f')
              
        if sensor['Tipo']=='co2':
                sensor['Valor']=format(sensor['Valor'],'.2f')

