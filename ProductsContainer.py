import json
from entity.Product import Product

class ProductsContainer:
	def __init__(self):
		self.__products = [];
		pass

	# Append product
	def append(self, product):
		if type(product) is Product:
			self.__products.append(product);
			return True
		elif type(product) is dict:
			self.append(self.input_normalize(product))
			return True
		return False
		pass

	def input_normalize(self, product_type_dict):
		product = Product()
		product.init_from_dict(product_type_dict)
		return product
		pass

	def get_item(self, inx):
		return self.__products[inx]
		pass

	def get_all(self):
		return self.__products;
		pass

	def to_json(self):
		return json.dumps({'products': self.products})
		pass

	def len(self):
		return len(self.__products);
		pass

	pass