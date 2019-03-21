import requests
import json
from entity.Product import Product
from ProductsContainer import ProductsContainer

class Parser:

	html = None

	def __init__(self):
		pass

	def search(self, query):
		if query:
			self.make_request('https://www.olx.ua/list/q-' + query + '/')
			return self.getProdList()
		else:
			print("getNewProdListError: wrong query!")
			return False 

	# https://www.olx.ua/uk/list/q-samsung/
	def make_request(self, url):
		response = requests.get(url)
		self.html = str(response.text)

	def getProdList(self):
		keysList = ["photo", "title", "page", "price", "id", "price_unit", "description", \
		"is_advertising", "region", "location", "timestamp"]
		resDict = {}
		resDictList = []
		htmlSplitByWrap = self.html.split("class=\"wrap\"")
		resStr = []  # img, link, title, price
		# storage for products
		prodsStorage = ProductsContainer()
		# Make data template
		prod = Product()

		for i in htmlSplitByWrap:
			l = i.split("<")

			for k in l:
				imgUrl = None
				link = None
				title = None
				price = None
				
				
				subStr = "img class=\"fleft\" src=\""
				subStr2 = " alt=\""

				begSrc = k.find(subStr)
				begSrc2 = k.find(subStr2)

				if begSrc != (-1):
					begSrc+=len(subStr)
					begSrc2+=len(subStr2)
					endSrc = k.find(";s=261x203", begSrc + 1)
					endSrc2 = k.find("\">", begSrc2 + 1)
					imgUrl = k[begSrc : endSrc]
					title = k[begSrc2 : endSrc2]
					# print("imgUrl:", imgUrl)
					# print("title:", title)
					resStr.append(imgUrl) # img url
					resStr.append(title) # img title
					prod.title = title
					prod.thumb = imgUrl  # whtf (thumb?)
					
				begLink = k.find("a href=\"https://www.olx.ua/obyavlenie/")
				if begLink != (-1):
					begLink = k.find("https://")
					endLink = k.find(".html", begLink + len("https://")) + 5  # 5 len(".html")
					link = k[begLink : endLink]
					# print("link:", link)
					resStr.append(link)  # link
					prod.url = link

				# add "free", "change", different currency
				begPrice = k.find("strong>")
				if begPrice != (-1) and k[-1] == '.':
					tmpLen = len("strong>")
					price = k[tmpLen : len(k) - 1]
					# print("price:", price)
					resStr.append(price)  # title or price
					prod.price = 99.99  # just for test

			if len(resStr) == 4:
				# Eugene's data struct
				prodsStorage.append(prod)
				print("prodsStorage", prodsStorage.len())

				# create dict
				for i in range(len(resStr)):
					resDict.update({ keysList[i]: resStr[i]})
				resDictList.append(dict(resDict))  # hard copy of dict obj
				resStr.clear()

		# print(self.toJson({"result": resDictList}))
		return self.toJson({"result": resDictList})

	def toJson(self, data = None):
		if data is not None:
			# data = {}
			# data['key'] = 'value'
			json_data = json.dumps(data, ensure_ascii=False)
		else:
			print("toJsonError: wrong data!")
			return False

		return json_data
						