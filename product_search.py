
#this is where we get the product keyword from (text_response.message_body) = entire message body - how to parse to find product. (message body is currently
	# of type unicode..)

from amazon.api import AmazonAPI
#insert amazon web services credentials
AMAZON_ACCESS_KEY = 'AKIAJHEHJV7E6JHDWGGA'
AMAZON_SECRET_KEY = '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'
#associate TAG must be updated every 180 days, make new amazon associates account to get new tag
AMAZON_ASSOC_TAG = 'ignacio0ba-20'

class Item(object):
	
	def __init__(self, product):
		self.product = product
		self.amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOC_TAG)

	def prod_search(self):
		products_found = self.amazon.search_n(1, Keywords= self.product, SearchIndex= "All")
		return products_found


	def prod_item(self):

		products_found = self.prod_search()
		try: 
			return products_found[0].title
		except IndexError:
			raise Exception('No product found')		

	def prod_asin(self):


		products_found = self.prod_search()
		try: 
			return products_found[0].asin
		except IndexError:
			raise Exception('No Asin found')	

	def prod_price(self):

		product_asin = self.prod_asin()
		the_product = self.amazon.lookup(ItemId='' + product_asin + '')
		found_product_price = the_product.price_and_currency
		return found_product_price



#customer_product = Item('uranium')
#customer_product = Item(product)

product_name = customer_product.prod_item()
#print product_name
product_asin = customer_product.prod_asin()
#print product_asin

product_price_and_currency = customer_product.prod_price()
#print product_price_and_currency

	


