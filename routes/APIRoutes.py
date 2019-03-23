from Parser import Parser
from flask import request
import json

def APIRoutes(app):
	@app.route("/rest-api/v1/search", methods = ['GET'])
	def search():
		P = Parser()
		query = request.args.get('query')	

		ProductsContainer = P.search(query)

		return ProductsContainer.to_json()
		pass