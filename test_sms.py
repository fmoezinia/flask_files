

#this solely sends out messages to specific number

from twilio.rest import TwilioRestClient


def send(result, customer):

	account_sid = "AC26a76547a74db155c8c9fa8a27293047"
	auth_token  = " 6158f22e6e884307f2553706444375ad "
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(body= result, to= customer, from_= "+16507279462")
	

# 	#print message.sid