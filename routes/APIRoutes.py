from Parser import Parser
from flask import request
from AltParser import AltParser
import json

def APIRoutes(app):

	@app.route("/rest-api/v1/search", methods = ['GET'])
	def search():
		P = Parser()
		word = request.args.get('word')		
		P.keyWord(word)
		P.resp()
		return P.hi()
		pass

	@app.route("/rest-api/v0/search", methods = ['GET'])
	def _search():
		altparser = AltParser(query = request.args.get('query'))
		products = altparser.get_prods_from_page()
		return json.dumps({"result": products});
		pass

	pass