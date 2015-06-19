#"""Respond to incoming calls with a simple text message."""

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def hello_monkey(): 
	
	print request.form
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey. this is a test. if you are hearing this, then the configuration has worked.")
	return str(resp)
  
@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def test():
 	return 'hello world' 

@app.route("/", methods=['GET', 'POST'])
def test():
 	return 'hello world' 	
 

if __name__ == "__main__":
	app.run(debug=True)
    #app.run(host = '0.0.0.0')