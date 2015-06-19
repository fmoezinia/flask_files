#this script has an automated voice to respond to callers

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def call(): 
	#"""Respond to incoming calls with a simple text message."""
	print request.form
	resp = twilio.twiml.Response()
	resp.say("Hello, Mobile Monkey. this is a test. if you are hearing this, then the configuration has worked.")
	return str(resp)
   

if __name__ == "__main__":
	app.run(debug=True)
    #app.run(host = '0.0.0.0')