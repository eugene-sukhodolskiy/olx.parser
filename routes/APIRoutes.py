from Parser import Parser
from flask import request
from AltParser import AltParser
import json

def APIRoutes(app):
	@app.route("/rest-api/v1/search", methods = ['GET'])
	def search():
		P = Parser()
		query = request.args.get('query')	

		ProductsContainer = P.search(query)

		# distplay it via console
		# Items = ProductsContainer.get_all()
		# for Item in Items:
		# 	Item.to_display()

		return ProductsContainer.to_json()
		pass

	@app.route("/rest-api/v0/search", methods = ['GET'])
	def _search():
		altparser = AltParser(query = request.args.get('query'))
		products = altparser.get_prods_from_page()
		return products.to_json()
		pass

	pass
