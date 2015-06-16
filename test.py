from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def test():
 	return 'hello ricky test'


if __name__ == "__main__":
	app.run(debug=True)
    app.run(host = '0.0.0.0', port=80)