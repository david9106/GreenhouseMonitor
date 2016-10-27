#Wireless sensor network applied to greenhouse monitoring via cloud access

The overall objective of the project (Wireless sensor network applied to
access via cloud monitoring greenhouse) is monitoring a
greenhouse through integrated sensors microcontroller
which can measure temperature, humidity, light and carbon dioxide
in the environment, such information will be collected, analyzed and adjusted by a
Raspberry Pi, then the information will be sent to a server for
so it can be viewed in graphs via internet through
a web browser.


##WSN (Wireless sensor network )
The [WSN (Wireless Sensor Network)](https://github.com/david9106/IS-Repo-Equipo2/tree/master/WSN) library is responsible for the reception,
transmission and adjustment of the information submitted by the senseores.
It is also responsible for handling battery alerts and shipments to
server.

Contents:
* lisandra_receiver: Module for receiving information on measurements made by the sensors
* lisandra_transmitter: Module responsible for sending information on measurements made by the sensors
* [rpi](https://github.com/david9106/IS-Repo-Equipo2/tree/master/WSN/rpi): Module responsible for alerts,processing and sending measurements data to the server

##Appengine
The library [appengine](https://github.com/david9106/IS-Repo-Equipo2/tree/master/appengine) the party will serve as a server, take charge
analyze, decode, store and graph the information submitted by the
RPI, will also be handling phone alerts if are met
certain conditions relating to limits established.

Contents:
* [Database](https://github.com/david9106/IS-Repo-Equipo2/tree/master/appengine/Database): Module responsible for the structure of the Data Base
* [Handlers](https://github.com/david9106/IS-Repo-Equipo2/tree/master/appengine/Handlers): Module responsible for handling database tasks, alerts and decoding json data
* [Templates](https://github.com/david9106/IS-Repo-Equipo2/tree/master/appengine/Templates): It contains files and controls that will be displayed in the web browser


##3rd party libs

* Twilio, for sending phone messages
* httplib2 for htttp requests
* pytz and six.py for Twilio dependencies


##python_utils
[python_utils](https://github.com/david9106/IS-Repo-Equipo2/tree/master/python_utils) it is a library used for the sole purpose of testing.



## API Reference
* [Google App Engine](https://cloud.google.com/appengine/docs)
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Twilio](https://www.twilio.com/) - voice & video messaging
* [Amcharts](https://www.amcharts.com/) - JavaScript Charts & Maps
* [Arduino](https://www.arduino.cc/) - Microcontrollers programming
	
##Authors
 - G. Karosuo
 - Islas Alejandro
 - Gutierrez David F.
 - Gutierrez Martin
 - Blanco Erick V.