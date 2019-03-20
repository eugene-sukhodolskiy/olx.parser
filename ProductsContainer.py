import json
from entity.Product import Product

class ProductsContainer:
	def __init__(self):
		self.__products = [];
		pass

	# Append product
	def append(self, product):
		if type(product) is Product:
			if not self.already_exists(product):
				self.__products.append(product);
				return True
			else:
				return False
		elif type(product) is dict:
			self.append(self.input_normalize(product))
			return True
		return False
		pass

	# Normalize input data
	def input_normalize(self, product_type_dict):
		product = Product()
		product.init_from_dict(product_type_dict)
		return product
		pass

	# Get one product item by index
	def get_item(self, inx):
		return self.__products[inx]
		pass

	# Get all products
	def get_all(self):
		return self.__products;
		pass

	# Convert to json
	def to_json(self):
		prepare = []
		for prod in self.__products:
			prepare.append(prod.to_dict())
			pass
		return json.dumps({'products': prepare})
		pass

	# Get total products
	def len(self):
		return len(self.__products);
		pass

	# Print to console
	def to_display(self):
		for item in self.__products:
			item.to_display()
			print("-----------")
			pass
		pass

	# Check for existence in this container
	def already_exists(self, product):
		matches = filter(lambda item: product.url == item.url, self.__products)
		if len(list(matches)) > 0:
			return True;
		return False
		pass

	pass