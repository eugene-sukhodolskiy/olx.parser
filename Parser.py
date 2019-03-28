import requests
import json
from entity.Product import Product
from ProductsContainer import ProductsContainer
from bs4 import BeautifulSoup

class Parser:

	html = None
	prodsStorage = None

	def __init__(self):
		pass

	def search(self, query, additional_query = ""):
		if query is not None:  # query isn't empty

			if self.is_exist():  # page is exist
				self.make_request('https://www.olx.ua/uk/list/q-' + query + '/' + additional_query)
				# self.make_request('https://www.olx.ua/uk/list/q-' + query + '/?search%5Border%5D=filter_float_price%3Aasc')  # min price
				# self.make_request('https://www.olx.ua/uk/list/q-' + query + '/?currency=USD')
				return self.get_products()
			else:
				return False  # page doesn't exist

		else:
			# print("get_products: Error: wrong query!")
			return False  # query is empty

	pass  # especially for Eugene ;-)

	# https://www.olx.ua/uk/list/q-samsung/
	def make_request(self, url):
		response = requests.get(url)
		self.html = str(response.text)

	pass  # especially for Eugene ;-)


	# get list of products (is automaticaly returned by self.search() method (if pages exist))
	def get_products(self):
		soup = BeautifulSoup(str(self.html), features = "lxml")

		# find tables list with products
		prods_src = soup.findAll("table", {"class": "breakword"})

		# storage for products
		prodsStorage = ProductsContainer()

		for item in prods_src:

			# Make data template
			prod = Product()

			# find title, url, is_promoted
			prod.title = item.find("td", {"class": "title-cell"}).find("a", {"class": "detailsLink"}).find("strong").text
			prod.url = item.find("td", {"class": "title-cell"}).find("a", {"class": "detailsLink"}).get("href")
			prod.is_promoted = False if prod.url.find(";promoted") == (-1) else True

			# find photo
			photo = item.find("img", {"class": "fleft"})
			if photo is not None:
				prod.thumb = photo.get("src")
				pass

			# find price and is_exchange
			price_container = item.find("p", {"class": "price"});
			if price_container is not None:
				price_src = price_container.find("strong").text.split(' ')
				if price_src[0].find("Обмін") > -1: 
					# print("Обмін")
					prod.price = 0.0
					prod.is_exchange = True
				elif price_src[0].find("Безкоштовно") > -1:
					# print("Безкоштовно")
					prod.price = 0.0
				else:
					tmp_str = ""
					for i in price_src:
						tmp_str += i
					prise_str = ''.join(c for c in str(tmp_str) if c.isdigit())
					prod.price = float(prise_str)
					tmp_currency = price_src[len(price_src)-1]
					if tmp_currency == "грн.":
						prod.currency = tmp_currency[:-1]
					else:
						prod.currency = tmp_currency
					pass
				pass

			# find category, timestamp, location
			tmpList = []
			temp_container = item.findAll("small", {"class": "breadcrumb x-normal"})
			for i in temp_container:
				data_list = i.text.split("<i data-icon=\"")
				tmpList.append(data_list[0].strip())

			prod.category = tmpList[0]
			prod.location = tmpList[1]
			prod.timestamp = tmpList[2]


			# append data template to prods array
			prodsStorage.append(prod)
			pass

		return prodsStorage
		pass

	pass

	# get page with number (if exist)
	def get_page(self, query, page_number = 1):
		if page_number <= 1 and not isinstance(page_number, int):
			print("get_page: Error: wrong page number!")
			return None
		else:

			if self.is_exist(query):
				additional_query = "?page=" + str(page_number)
				return self.search(query, additional_query)
			else:
				# page doesn't exist
				return None

	pass  # especially for Eugene ;-)


	def is_exist(self, query):
		# <span class="marker">Перевірте правильність написання або введіть інші параметри пошуку</span>
		self.make_request('https://www.olx.ua/uk/list/q-' + query + '/')
		soup = BeautifulSoup(str(self.html), features = "lxml")
		not_found = soup.findAll("span", {"class": "marker"})
		not_exist_answer = "<span class=\"marker\">Перевірте правильність написання або введіть інші параметри пошуку</span>"

		if not_exist_answer in not_found:
			print("pages_ammount: Error: page doesn't exist:", not_found)
			return False
		return True

	pass  # especially for Eugene ;-)


	# also it is possible to use for checking whether pages for this request are exist (different method of checking)
	def pages_ammount(self, query):
		self.make_request('https://www.olx.ua/uk/list/q-' + query + '/')
		soup = BeautifulSoup(str(self.html), features = "lxml")
		# pages = soup.findAll("div", {"class": "pager rel clr"})
		ammount = soup.findAll("span", {"class": "item fleft"})

		try:
			str_max_number = ammount[-1].text
		except IndexError:
			print("pages_ammount: Error: pages for this query don't exist!")
			return False

		max_number = ''.join(c for c in str(str_max_number.split("<span>")) if c.isdigit()) 
		return max_number  # pages with results for current request

	pass  # especially for Eugene ;-)
						