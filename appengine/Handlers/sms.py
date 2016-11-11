##@file sms.py
#@brief This module is used to send the messages to user 
from twilio.rest import Client

account_sid = "AC0b80488af39dcd381ac952934507ef69" # Your Account SID from www.twilio.com/console
auth_token  = "617ce805fc5a06c6aabc9e3aaf3549bf"  # Your Auth Token from www.twilio.com/console

##@brief Used to send a message to user
#@details The function send a sms message using the twilio library functions
#@param phone_number: Has a string with the user phone numbers
#@param info: This parameter have a string with the message to send to the user
def sendMsg(telefono,info):
	client = Client(account_sid, auth_token)
	# replace "to" and "from_" with real numbers
	rv = client.messages.create(to="+52"+telefono,from_="+16179970349 ",body=info)