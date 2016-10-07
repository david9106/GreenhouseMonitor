import time
#archvio donde se guardaran las mediciones
f = "./measures.txt"
	
def write(data):
	#abrimos el archivo en modo agregar
	outfile = open(f,'a')
	#agregamos la informacion
	outfile.write(time.strftime("%X")+" "+data+'\n')
	outfile.close()
