

#this solely sends out messages to specific number

from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC26a76547a74db155c8c9fa8a27293047"
auth_token  = " 6158f22e6e884307f2553706444375ad "
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body=" This is a twilio sent message from Fred Ricky",
    to="7186121018",    # Replace with your phone number
    from_="+16507279462") # Replace with your Twilio number
#print message.sid