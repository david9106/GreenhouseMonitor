##Wireless sensor network applied to greenhouse monitoring via cloud access

Funciones implementadas:

*Comunicacion via RF entre módulos de sensado LiSANDRA.

*Comunicacion Serial entre lisandra y rpi.

*Sensado (raw)en lisandra emisor.

*Llenado de trama (bytes raw)en lisandra emisor.

*Recepcion de trama (bytes raw) y conversion a uint16_t en lisandra receptor.

*Conversion de valores seriales en unidades de medida en rpi.

*Agregado el modulo .py para enviar json

*Agregado el modulo .py para escribir en archivo (solo para pruebas)

*Receptor de módulos json en el server, por medio de requests POST

*Modelo de BD no relacional para guardar los datos sensados
