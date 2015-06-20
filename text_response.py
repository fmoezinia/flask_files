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
customer = None
result = None


@app.route("/my_twilio_endpoint", methods=['GET', 'POST'])
def reply():

	
	global state
	global asin
	global customer
	global result
	global message_body

#unicode to string
	message_body = request.form['Body']
	message_body = message_body.encode("utf-8", "ignore")
	customer = request.form['From']
	customer = customer.encode("utf-8", "ignore")

	print 'blah 1'
	if state == 'suggestion':

	#print message_body
		item = Item(message_body)
		print 'blah 0'
		txtresp = "We found this product : {0}. The price will be: {2} {1} (Can add image later). Respond 'yes' or 'Yes' if you would like to purchase this item".format(item.prod_item(), item.prod_price()[0], item.prod_price()[1])
		resp = twilio.twiml.Response()
		resp.message(txtresp)
		asin = str(item.prod_asin())
		state = 'purchase'
		
		#this return statement is needed to send response text - and also returns on web app
		return str(resp)
	
	#TEXT THEM A LINK TO FLASK WEB APP, DIFFERENT ENDPOINT ENTER CREDIT CARD (need variables in request amazon for deatials and biling creds)
		
		
	elif state == 'purchase':
		#FIX TO MAKE ALL YESES WITH LOWERCASE ETC
		if message_body == 'Yes':
			#buy product
			print 'blah 3'
			state = 'confirmation'
			request_amazon.buy(asin)
			asin = None
			result = 'Your order has been processed and is on its way!'
			#MUST RETURN SOMETING?
			return 'hi'
		else:
			print 'blah 6'
			state = 'suggestion'
			result = 'We are sorry that you do not want to purchase this item. Please search for a different product!'
			test_sms.send(result, customer)
			customer = None
			result = None
			return 'hi'

	elif state == 'confirmation':
		#did all go well?
		print 'blah 5'
		test_sms.send(customer,result)
		customer = None
		state = 'suggestion'
		result = None
		#MUST RETURN SOMETING?		
		return 'hi'


if __name__ == "__main__":
    app.run(debug = True, port=80, host = '0.0.0.0')

 #message_body is content. 