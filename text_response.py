#this script responds to texts, and takes message body (prints to webpage)


from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)


@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def reply():


	#print request.form
	
	message_body = request.form['Body']
	#print message_body

	resp = twilio.twiml.Response()
	resp.message('Hello, we got your text')
	#this return statement is needed to send response text - and also returns on web app
	return str(resp)


	


if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')