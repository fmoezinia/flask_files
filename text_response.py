#this script responds to texts, and takes message body (prints to webpage)


from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)


@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def test():


	print request.form
	#prints message body
	print 'message below'
	print request.form['body']
	print "message above"

	resp = twilio.twiml.Response()
	resp.message("Hello, we got your text")
	return str(resp)

	#this prints response on web server darkside
	print resp


if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')