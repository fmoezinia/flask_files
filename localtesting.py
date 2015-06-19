#this script responds to texts, and takes message body (prints to webpage)


from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def test():


	print request.form
	#prints message body
	print request.form['body']

	resp = twilio.twiml.Response()
	resp.message("Hello, we got your text")
	return str(resp)

	#this prints response on web server darkside
	print resp


if __name__ == "__main__":
    app.run(debug = True)