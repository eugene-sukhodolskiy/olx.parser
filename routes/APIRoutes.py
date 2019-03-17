from Parser import Parser

def APIRoutes(app):

	@app.route("/rest-api/v1/search")
	def search():
		parser = Parser();
		return parser.hi()
		pass	

	pass