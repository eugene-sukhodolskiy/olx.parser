import requests
import json
from entity.Product import Product
from ProductsContainer import ProductsContainer
import copy

class Parser:

	html = None
	prodsStorage = None

	def __init__(self):
		pass

	def search(self, query):
		if query:
			self.make_request('https://www.olx.ua/list/q-' + query + '/')  # ?currency=USD
			# self.make_request('https://www.olx.ua/list/q-' + query + '/?currency=USD')
			return self.getProdList()
		else:
			print("getNewProdListError: wrong query!")
			return False 

	# https://www.olx.ua/uk/list/q-samsung/
	def make_request(self, url):
		response = requests.get(url)
		self.html = str(response.text)

	def getProdList(self):
		keysList = ["photo", "title", "page", "price", "currency", "id", "price_unit", "description", \
		"is_advertising", "region", "location", "timestamp"]
		resDict = {}
		resDictList = []
		htmlSplitByWrap = self.html.split("class=\"wrap\"")
		resStr = []  # img, link, title, price
		# storage for products
		self.prodsStorage = ProductsContainer()
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
					if endSrc == (-1):
						endSrc = k.find("\\", begSrc + 1)  # fix strange ending img Link
					# print("endSrc:", endSrc)
					endSrc2 = k.find("\">", begSrc2 + 1)
					imgUrl = k[begSrc : endSrc]
					title = k[begSrc2 : endSrc2]
					# print("imgUrl:", imgUrl)
					# print("title:", title)
					resStr.append(imgUrl) # img url
					resStr.append(title) # img title
					prod.title = title
					prod.thumb = imgUrl  # whtf (thumb?)
					# print(prod)
					
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
				curList = ["грн.", "$", "€", "Безкоштовно", "Обмін"]  # , "$", "€", "Безкоштовно", "Обмін"
				curExist = False
				currency = ""
				for cur in curList:
					if k.find(cur) != (-1):
						curExist = True
						if cur == "грн.":
							currency = cur[:-1]  # remove point in "грн." 
						else:
							currency = cur  # "€" e.x.
				if begPrice != (-1) and curExist:
				# if begPrice != (-1) and k[-1] == '.':
					tmpLen = len("strong>")
					if str(k[tmpLen]).isdigit():
						if k.find("грн.") != (-1):
							price = ''.join(c for c in str(k[tmpLen : len(k) - 5]) if c.isdigit())  # remove all signs exept digits
						else:
							price = ''.join(c for c in str(k[tmpLen : len(k) - 2]) if c.isdigit())  # remove all signs exept digits
						# print("price:", price)
						# print("currency:", currency)
						resStr.append(price)  # price
						resStr.append(currency)
						# print("price is ready")

						prod.price = price
						prod.price_unit = currency
						# print(prod.price)

				if len(resStr) == 5:  # lose data in case of product without price
					# Eugene's data struct
					self.prodsStorage.append(copy.deepcopy(prod))
					# print("prodsStorage", prodsStorage.len())

					# create dict
					for i in range(len(resStr)):
						resDict.update({ keysList[i]: resStr[i]})
					resDictList.append(copy.deepcopy(dict(resDict)))  # hard copy of dict obj
					resStr.clear()

		# print(self.toJson({"result": resDictList}))
		# tmp = prodsStorage.get_all()
		# for lol in tmp:
		# 	print("title", lol.title)
		print("prodsStorage.len():", self.prodsStorage.len())
		return self.toJson({"result": resDictList})

	def getProd(self):  # call it only after self.getProdList() -> return None (if not)
		# return copy.deepcopy(self.prodsStorage)
		return self.prodsStorage

	def toJson(self, data = None):
		if data is not None:
			# data = {}
			# data['key'] = 'value'
			json_data = json.dumps(data, ensure_ascii=False)
		else:
			print("toJsonError: wrong data!")
			return False

		return json_data
						