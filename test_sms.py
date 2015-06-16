from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC26a76547a74db155c8c9fa8a27293047"
auth_token  = " 6158f22e6e884307f2553706444375ad "
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="This is a message for Monica Moezinia. \
	We have tried to get in touch with your son, Fredric, regarding his Royal College of Music application. Unfortunately, his UK mobile is unavailable. We would like to inform you that there was an error with his online application last June. Although he was accepted at the RCM, unfortunately, we did not get a receipt of his acceptance, meaning he was not offered a place. We recently updated our online IT support, and noticed the error. Please call the RCM at your own convenience.",
    to="+17186121018",    # Replace with your phone number
    from_="+16507279462") # Replace with your Twilio number
print message.sid