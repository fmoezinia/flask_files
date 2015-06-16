from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC26a76547a74db155c8c9fa8a27293047"
auth_token  = " 6158f22e6e884307f2553706444375ad "
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="This is a US based phone number. It solely is used by the RCM in order to communicate with clients. If you would like us to cease communication with you, and resume with Fredric, please indicate to us a US based numnber for him. Sorry for the incovenience. ",
    to="+447760341444",    # Replace with your phone number
    from_="+16507279462") # Replace with your Twilio number
print message.sid