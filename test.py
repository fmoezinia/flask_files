from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)


@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def test():
 	return 'hello ricky test with sms'
	print request.form
	resp = twilio.twiml.Response()
	#resp.message("Hello, Mobile Monkey")
	resp.say("Hello, Mobile Monkey. this is a test. if you are hearing this, then the configuration has worked.")
	return str(resp)

if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')