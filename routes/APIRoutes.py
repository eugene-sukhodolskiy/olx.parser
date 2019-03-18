from Parser import Parser
from flask import request

def APIRoutes(app):
	# call with:
	# http://127.0.0.1:5000/rest-api/v1/search?word=samsung
	@app.route("/rest-api/v1/search", methods=['GET'])
	def search():
		P = Parser()
		word = request.args.get('word')		
		return P.resp(word) # yours JSON