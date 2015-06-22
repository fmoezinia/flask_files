#this file will explore the twilio cookie platform; attempting to store information about user such as billing info and credit card details
#cookie is pertinent to a 2 number pair

from flask import Flask, request, redirect, session
import twilio.twiml
 
# The session object makes use of a secret key.
SECRET_KEY = 'fallafel'
app = Flask(__name__)
app.config.from_object(__name__)
 
# Try adding your own number to this list!
callers = {
    "+17186121018": "Ricky	",
    "+16507279462": "twilio",
    "+14158675311": "Virgil",
}
 
@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def hello_monkey():
    """Respond with the number of text messages sent between two parties."""
 
    counter = session.get('counter', 0)
 
    # increment the counter
    counter += 1
 
    # Save the new counter value in the session
    session['counter'] = counter
 
    from_number = request.values.get('From')
    if from_number in callers:
        name = callers[from_number]
    else:
        name = "Monkey"
 
    message = "".join([name, " has messaged ", request.values.get('To'), " ", str(counter), " times."])
    resp = twilio.twiml.Response()
    resp.sms(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')