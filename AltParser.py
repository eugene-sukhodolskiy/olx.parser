import requests
from bs4 import BeautifulSoup

class AltParser:
	html = False;

	def __init__(self, query):
		# make request and save response to self.html
		self.make_request('https://www.olx.ua/list/q-' + query + '/')
		# search data about products in response
		pass

	def make_request(self, url):
		response = requests.get(url)
		self.html = str(response.content)
		pass

	def get_prods_from_page(self):
		soup = BeautifulSoup(str(self.html), features = "lxml")

		# find tables list with products
		prods_src = soup.findAll("table", {"class": "breakword"})

		# storage for products
		prodsStorage = []

		prods_src_length = len(prods_src)
		print(prods_src_length)
		print(type(prods_src))
		i = 1
		while i <= 46:
			item = prods_src[i]
			i = i + 1
			print(i)

			# Make data template
			prod = {"title": "", "page": "", "photo": "", "price": ""}

			# find title and url to page
			prod["title"] = item.find("td", {"class": "title-cell"}).find("a", {"class": "detailsLink"}).find("strong").text
			prod["page"] = item.find("td", {"class": "title-cell"}).find("a", {"class": "detailsLink"}).get("href")

			# find photo
			photo = item.find("img", {"class": "fleft"})
			if photo is not None:
				prod["photo"] = photo.get("src")
				pass

			# find price
			price_container = item.find("p", {"class": "price"});
			if price_container is not None:
				prod["price"] = price_container.find("strong").text
				pass

			# append data template to prods array
			prodsStorage.append(prod)
			pass

			print(len(prodsStorage))

			return prodsStorage
		pass

	pass

# Run
# altparse = AltParser('iphone')
# products = altparse.get_prods_from_page();
