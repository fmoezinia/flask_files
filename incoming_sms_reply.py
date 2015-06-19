# this script replies to texts
# ssh zincadm@104.236.14.203 -p 3192    this is my darkside server with flask web app
# ti1sPWD sudo python script

from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+17186121018": "Curious Ricky",
    "+15107980598" : "Monsieur Wu"}
 
@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def hello_monkey():
 
    from_number = request.values.get('From', None)
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 #change
if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')