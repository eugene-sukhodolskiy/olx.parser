from Parser import Parser
from flask import request
from AltParser import AltParser
import json

def APIRoutes(app):
	@app.route("/rest-api/v1/search", methods = ['GET'])
	def search():
		P = Parser()
		query = request.args.get('query')	
		JSON_from_Parcer = P.search(query)

		ProdContainer = P.getProd()  # call it only after P.search(query)
		ProdList = ProdContainer.get_all()	
		print(ProdList[0].to_display())
		return JSON_from_Parcer # yours JSON
		pass

	@app.route("/rest-api/v0/search", methods = ['GET'])
	def _search():
		altparser = AltParser(query = request.args.get('query'))
		products = altparser.get_prods_from_page()
		return products.to_json()
		pass

	pass
