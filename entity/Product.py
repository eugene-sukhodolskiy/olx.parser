class Product:
	def __init__(self):
		# Title of product
		self.title = ""

		# Url to page with product
		self.url = ""

		# Url to product photo
		self.thumb = ""

		# Price of product
		self.price = 0.0

		# Description of product
		self.description = ""

		# Flag if product is advertising
		self.is_advertising = False;

		# Product location
		self.city = ""

		# When product posted
		self.timestamp = ""
		pass

		def init_from_dict(self, dict_item):
			if type(dict_item) is not dict:
				return False;

			try:
				props = list(dict_item.keys());
				for i in props:
					if type(self[i]) == type(dict_item[i]):
						self[i] = dict_item[i]
					else:
						raise BadType()
					pass
				pass
			except BadType:
				print("Bad type")
				pass

			pass
	pass