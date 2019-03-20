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

		# Unit of price
		self.price_unit = ""

		# Description of product
		self.description = ""

		# Flag if product is advertising
		self.is_advertising = False;

		# Product location
		self.region = ""  # Zhytomyr
		self.location = ""  # Bila Tserkva

		# When product posted
		self.timestamp = ""
		pass

	# Initialize fields from dict
	def init_from_dict(self, dict_item):
		if type(dict_item) is not dict:
			return False;

		try:
			props = list(dict_item.keys());
			for i in props:
				# Check type on correctly
				if type(self.__dict__[i]) == type(dict_item[i]):
					self.__dict__[i] = dict_item[i]
				else:
					# Generate exception
					raise BadType()
				pass
			pass
		except BadType:
			print("Bad type")
			pass

		pass

	# Transform this object to dictonary
	def to_dict(self):
		return self.__dict__;
		pass

	# Print to console
	def to_display(self):
		for prop in self.__dict__:
			print(prop, ": ", self.__dict__[prop])
		pass

	pass