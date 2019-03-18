from Parser import Parser
from flask import request

def APIRoutes(app):
	# http://127.0.0.1:5000/rest-api/v1/search?word=125
	@app.route("/rest-api/v1/search", methods=['GET'])
	def search():
		P = Parser()
		word = request.args.get('word')		
		P.keyWord(word)
		print(P.resp())  # yours JSON
		return P.hi()