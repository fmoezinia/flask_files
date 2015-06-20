#this script responds to texts, and takes message body (prints to webpage)
import test_sms
import request_amazon
import unicodedata
from flask import Flask, request, redirect
import twilio.twiml


#can now use item classes from product search.
from product_search import Item
 
app = Flask(__name__)

#item needs to contain the product asin when it runs thorugh the clause
asin = None
# 3 states: suggestion, purchase, and confirmation
state = 'suggestion'
client = None



@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def reply():

	#print request.form
	
	message_body = request.form['Body']
	#CHANGE MESSAGE BODY INTO STRING....!!!
	message_body = message_body.encode("utf-8", "ignore")
	global state
	global asin
	global client

	if state == 'suggestion':

	#print message_body
		item = Item(message_body)

		txtresp = "We found this product : {0} at: {2}{1} (and image). Respond 'yes' if you would like to purchase this item".format(item.prod_item(), item.prod_price()[0], item.prod_price()[1])
		resp = twilio.twiml.Response()
		resp.message(txtresp)
		asin = item.prod_asin()
		state = 'purchase'
		client = request.form['From']
		#CHANGE client !!! BODY INTO STRING....!!!
		client = client.encode("utf-8", "ignore")
		#this return statement is needed to send response text - and also returns on web app
		return str(resp)

	
	#TEXT THEM A LINK TO FLASK WEB APP, DIFFERENT ENDPOINT ENTER CREDIT CARD (need variables in request amazon for deatials and biling creds)
		
		
	elif state == 'purchase':
		if message_body == ('yes' or 'Yes' or 'YES'):
			#buy product
			state = 'confirmation'
			#import request_amazon. call function where asin = item.prod_asin()
			result = request_amazon.buy(asin)
			asin = None
			#MUST RETURN SOMETING?
			return 'hi'
		else:
			state = 'confirmation'
			result = 'We are sorry that you do not want to purchase this item. Please'

	elif state == 'confirmation':
		#did all go well?
		test_sms.send(client,result)
		client = None
		state = 'suggestion'
		#MUST RETURN SOMETING?		
		return 'hi'


if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')

 #message_body is content. 