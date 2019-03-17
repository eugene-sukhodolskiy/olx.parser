from Parser import Parser
from flask import request

def APIRoutes(app):

	@app.route("/rest-api/v1/search", methods=['GET'])
	def search():
		P = Parser()
		word = request.args.get('word')		
		P.keyWord(word)
		P.resp()
		return P.hi()