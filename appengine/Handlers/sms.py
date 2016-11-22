##@file sms.py
#@brief This module is used to send the messages to user 
from twilio.rest import Client

account_sid = "AC60d43ab9482bb26027ae83cb8b356705" # Your Account SID from www.twilio.com/console
auth_token  = "0bc50ddd92fde73507b42ca6de2375e9"  # Your Auth Token from www.twilio.com/console

##@brief Used to send a message to user
#@details The function send a sms message using the twilio library functions
#@param phone_number: Has a string with the user phone numbers
#@param info: This parameter have a string with the message to send to the user
def sendMsg(telefono,info):
	try:
		client = Client(account_sid, auth_token)
		# replace "to" and "from_" with real numbers
		rv = client.messages.create(to="+52"+telefono,from_="+1 402-718-8732  ",body=info)
	except Exception as e:
		print("General EXCEPTION thrown: {!s}".format(e))	
