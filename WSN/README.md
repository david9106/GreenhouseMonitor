#Wireless sensor network  - WSN

This module is responsible for the reception 
and transmission of data between sensors 
(Microcontrollers Lisandra) and the gateway 
(Raspberry Pi 2 Model B), it is also 
responsible for sending the information to the 
server in JSON format and handle phone 
email updates the battery.

#Getting Started
These instructions will get you a copy of the project up 
and running on your Raspberry.

#Prerequisites

A computer with windows and Raspberry Pi 2 Model B

First needs install python on your rpi (if it is already installed 
you can skip this step):

$ sudo apt-get install python3 
or 
$sudo apt-get install python


You also need to install [pySerial](https://pythonhosted.org/pyserial/) on your Raspberry Pi running the next command:

$ sudo apt-get install python-serial
or
$ sudo apt-get install python3-serial

then execute de following commands:

$ sudo nano /boot/config.txt

Add at bottom the next line:

"enable_uart=1" without quotation marks

$ sudo nano /boot/cmdline.txt

Delete "console=serial0,115200" and reboot RPI


You must also install [request library](http://docs.python-requests.org/en/master/) :

$ pip install requests


To program the Lisandra Microcontrollers you need arduino arduino-1.6.11 on your computer
and modify the next:

-boards.txt

-platform.txt

-programmers.txt


#Installing

Copy the folder rpi to your Raspberry Pi home folder.

Copy the folders lisandra_receiver and transmitter to your desktop.


#Running the tests

In arduino set options Tools->Board->LISANDRA-R,Tools->Porcessor->ATmega644p or ATmega12844p
according your version,Tools->Programmer->LISANDRA 19.2k(644p) or LISANDRA 38.4k(644p).

Once you have done this:

Open transmitter on lisandra_transmitter folder and program Lisandra.

Open receiver on lisandra_receiver folder and program another Lisandra.

Connect lisandra receiver to rpi GPIO
Lisandra		RPI
v+				Pin 1
rx				Pin 8
gnd -			Pin 9
tx				Pin 10

Then in your Raspberry Pi navigate to the folder rpi and execute

$ python receptor.py


You will see in console the number of packets and measures received from Lisandras and
json's sent to the server.


## Functions
Lisandra
-	decodeData: This function decode raw data received from Lisandra transmitter
-	sendData: This function sends decoded data to RPI serial ports
-	llenaTrama: Build a packet with raw data form sensors
Raspberry Pi
-	receptor: This module receive data from serial ports
-	parser: This module converts raw data to list of sensors
-   conversor: This module adjust the values to real measure form each sensor
-	sendToServer: This module converts list of sensor in JSON object an sent to the server
-	sms: this module handle the phone alerts

## Built With
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [Twilio](https://www.twilio.com/) - voice & video messaging
* [Arduino](https://www.arduino.cc/) - Microcontrollers programming
	
##Authors
 - G. Karosuo
 - Islas Alejandro
 - Gutierrez David F.
 - Gutierrez Martin
 - Blanco Erick V.



