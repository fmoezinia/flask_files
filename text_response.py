#this script responds to texts, and takes message body (prints to webpage)


from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)


@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def test():


	print request.form
	
	message_body = request.form['Body']


	resp = twilio.twiml.Response()
	resp.message("Hello, we got your text")
	#this prints response on web server darkside	
	return str(resp)

	


if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')