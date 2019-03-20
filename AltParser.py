import requests
from bs4 import BeautifulSoup
from entity.Product import Product
from ProductsContainer import ProductsContainer

class AltParser:
	html = False;

	def __init__(self, query):
		# make request and save response to self.html
		self.make_request('https://www.olx.ua/list/q-' + query + '/')
		pass

	def make_request(self, url):
		response = requests.get(url)
		self.html = str(response.text)
		pass

	# search data about products in response
	def get_prods_from_page(self):
		soup = BeautifulSoup(str(self.html), features = "lxml")

		# find tables list with products
		prods_src = soup.findAll("table", {"class": "breakword"})

		# storage for products
		prodsStorage = ProductsContainer()

		for item in prods_src:

			# Make data template
			prod = Product()

			# find title and url to page
			prod.title = item.find("td", {"class": "title-cell"}).find("a", {"class": "detailsLink"}).find("strong").text
			prod.url = item.find("td", {"class": "title-cell"}).find("a", {"class": "detailsLink"}).get("href")

			# find photo
			photo = item.find("img", {"class": "fleft"})
			if photo is not None:
				prod.thumb = photo.get("src")
				pass

			# find price
			price_container = item.find("p", {"class": "price"});
			if price_container is not None:
				price_src = price_container.find("strong").text.split(' ')[0]
				if price_src.find("Обмен") > -1:
					prod.price = 0.0
				else:
					prod.price = float(price_src)
					pass
				pass

			# append data template to prods array
			prodsStorage.append(prod)
			pass

		return prodsStorage
		pass

	pass

# Run (For test)
# altparse = AltParser('iphone')
# products = altparse.get_prods_from_page();
