from flask import render_template

def WebRoutes(app):
	@app.route("/")
	def home_page():
		return render_template("home.html")
		pass

	@app.route("/about")
	def about_page():
		return render_template('about.html')
		pass
	pass