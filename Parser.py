import requests
import json


class Parser:

	def __init__(self):
		pass

	def resp(self, word):
		keysList = ["photo", "title", "page", "price"]
		resDict = {}
		resDictList = []
		numberOfElem = 0
		response = requests.get('https://www.olx.ua/list/q-' + word + '/')  # https://www.olx.ua/uk/list/q-samsung/
		a = response.text
		b = a.split("class=\"wrap\"")
		resStr = []  # img, link, title, price
		for i in b:
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
				# endSrc = 0

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
					resStr.append(title) # img url
					
				begLink = k.find("a href=\"https://www.olx.ua/obyavlenie/")
				if begLink != (-1):
					begLink = k.find("https://")
					endLink = k.find(".html", begLink + len("https://")) + 5  # 5 len(".html")
					link = k[begLink : endLink]
					# print("link:", link)
					resStr.append(link)  # link

				begPrice = k.find("strong>")
				# print("begPrice", begPrice)
				if begPrice != (-1) and k[-1] == '.':
					tmpLen = len("strong>")
					price = k[tmpLen : len(k) - 1]
					# print("price:", price)
					resStr.append(price)  # title or price

			if len(resStr) == 4:
				# create dict
				for i in range(len(resStr)):
					resDict.update({ keysList[i]: resStr[i]})
				resDictList.append(dict(resDict))  # hard copy of dict obj
				resStr.clear()

		print(self.toJson({"result": resDictList}))
		return self.toJson({"result": resDictList})
		# return "test"

	def toJson(self, data = None):
		if data is not None:
			# data = {}
			# data['key'] = 'value'
			json_data = json.dumps(data)
		else:
			print("toJson:", "Error: wrong data!")

		return json_data
						