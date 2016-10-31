from twilio.rest import Client

account_sid = "AC0b80488af39dcd381ac952934507ef69" # Your Account SID from www.twilio.com/console
auth_token  = "617ce805fc5a06c6aabc9e3aaf3549bf"  # Your Auth Token from www.twilio.com/console

def sendMsg(telefono,info):
	client = Client(account_sid, auth_token)
	# replace "to" and "from_" with real numbers
	rv = client.messages.create(to="+52"+telefono,from_="+16179970349 ",body=info)