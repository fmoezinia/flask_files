
import requests
import product_search
from amazon.api import AmazonAPI
#python request http request
#to https://api.zinc.io/v0/order
#curl https://api.zinc.io/v0/order -d
import ssl


#post_api_request = requests.post(url, json = info)


# print (post_api_request.status_code)
def buy(asin):
	url = "https://api.zinc.io/v0/order"
	info = {"client_token": "597348b9c4452620817acf4a","retailer": "amazon", "products": [{"product_id": asin, "quantity": 1}],"max_price": 0, "shipping_address": {  "first_name": "Fredric",  "last_name": "Moezinia",   "address_line1": "18 Cliffview Drive",  "address_line2": "",  "zip_code": "07848","city": "Lafayette",   "state": "NJ",  "country": "US",  "phone_number": "7186121018"}, "is_gift": True, "gift_message": "Heres your package, Tim! Enjoy!", "shipping_method": "cheapest", "payment_method": {  "name_on_card": "Fredric Moezinia",  "number": "372325757571022",  "security_code": "2338",  "expiration_month": 3,  "expiration_year": 2022,  "use_gift": False },"billing_address": {  "first_name": "William",    "last_name": "Rogers",  "address_line1": "84 Massachusetts Ave",   "address_line2": "",  "zip_code": "02139",  "city": "Cambridge",   "state": "MA",  "country": "US",  "phone_number": "5551234567"}, "retailer_credentials": {  "email": "moezinia.r@gmail.com",  "password": "q2wq2wq2w"},"webhooks": {  "order_placed": "http://mywebsite.com/zinc/order_placed",  "order_failed": "http://mywebsite.com/zinc/order_failed",  "tracking_obtained": "http://mywebsite.com/zinc/tracking_obtained" },"client_notes": {  "our_internal_order_id": "abc123"}}

	if requests.post(url, json = info).status_code == 200:
		post_api_request = requests.post(url, json = info)
	else:
		print post_api_request.raise_for_status()
		raise Exception("Order not processed")




# #   r.status_code  == 404 is bad, raise excpetion etc, None = all is well  TRY EXCPET, RAISE
# #response 200 if ok
# #If we made a bad request (a 4XX client error or 5XX server error response), we can raise it with Response.raise_for_status():



