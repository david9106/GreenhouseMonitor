##@file sms.py
#@brief This module is used to send the messages to user 
from twilio.rest import Client

account_sid = "AC1118e1183377c9bb4e1481ab130f2c9e" # Your Account SID from www.twilio.com/console
auth_token  = "bb95a87926c196f15a71f9af764c45a9"  # Your Auth Token from www.twilio.com/console

##@brief Used to send a message to user
#@details The function send a sms message using the twilio library functions
#@param phone_number: Has a string with the user phone numbers
#@param info: This parameter have a string with the message to send to the user
def sendMsg(telefono,info):
	client = Client(account_sid, auth_token)
	# replace "to" and "from_" with real numbers
	rv = client.messages.create(to="+52"+telefono,from_="+19106726675 ",body=info)
