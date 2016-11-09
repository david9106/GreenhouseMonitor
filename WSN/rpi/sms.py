## @file sms.py
# @brief This module is responsible sending phone alerts.
# This module is used to send an alert to a phone number.
# 
from twilio.rest import TwilioRestClient
account_sid = "AC0b80488af39dcd381ac952934507ef69" # @var Your Account SID from www.twilio.com/console
auth_token  = "617ce805fc5a06c6aabc9e3aaf3549bf"  # @var Your Auth Token from www.twilio.com/console

## @brief The function "sdnMsg" sends an alert.
# Sends an alert to a phone number.
# @param "telefono" Phone receiving the message
# @return None
def sendMsg(telefono):
	client = TwilioRestClient(account_sid, auth_token)#protocolo para enviar msg
     
	message = client.messages.create(body="BATERIA BAJA",
	    to="+52"+telefono,    # @var Phone number
	    from_="+16179970349") # @var Twilio number

	print(message.sid+'\n')