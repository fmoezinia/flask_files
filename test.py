from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)


@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def test():
 	return 'hello ricky test'
	print request.form
	resp = twilio.twiml.Response()
	resp.message("Hello, Mobile Monkey")
	return str(resp)

if __name__ == "__main__":
	#app.run(debug=True)
    app.run(host = '0.0.0.0', port=80)