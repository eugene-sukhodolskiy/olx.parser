from flask import Flask

app = Flask(__name__)

from WebRoutes import WebRoutes
from APIRoutes import APIRoutes

WebRoutes(app)
APIRoutes(app)

app.run(debug = True)