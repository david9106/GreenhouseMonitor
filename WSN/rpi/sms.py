from twilio.rest import TwilioRestClient
#Script sms.py

account_sid = "AC0b80488af39dcd381ac952934507ef69" # Your Account SID from www.twilio.com/console
auth_token  = "617ce805fc5a06c6aabc9e3aaf3549bf"  # Your Auth Token from www.twilio.com/console

def sendMsg():
	client = TwilioRestClient(account_sid, auth_token)#protocolo para enviar msg
     
	message = client.messages.create(body="BATERIA BAJA",
	    to="+526645380095",    # Replace with your phone number
	    from_="+16179970349") # Replace with your Twilio number

	print(message.sid+'\n')