from flask import Flask

app = Flask(__name__)

from routes.WebRoutes import WebRoutes
from routes.APIRoutes import APIRoutes

WebRoutes(app)
APIRoutes(app)

app.run(debug = True)