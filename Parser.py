import requests
import json


class Parser:

	def __init__(self):
		pass

	def resp(self, word):
		keysList = ["photo", "page", "title", "price"]
		resDict = {}
		resDictList = []
		numberOfElem = 0
		response = requests.get('https://www.olx.ua/list/q-' + word + '/')  # https://www.olx.ua/uk/list/q-samsung/
		a = response.text
		b = a.split("class=\"wrap\"")
		resStr = []  # img, link, title, price
		for i in b:
			l = i.split(">\\n")
			# l = i
			for k in l:
				imgUrl = None
				link = None
				title = None
				price = None

				subStr = "<img class=\"fleft\" src=\""
				begSrc = k.find(subStr)
				endSrc = 0

				if begSrc != (-1):
					begSrc+=len(subStr)
					endSrc = k.find("\"", begSrc + 1)
					imgUrl = k[begSrc : endSrc]
					resStr.append(imgUrl) # img url
					
				begLink = k.find("<a href=\"https://www.olx.ua/obyavlenie/")
				if begLink != (-1):
					begLink = k.find("https://")
					endLink = k.find("\"", begLink + len("https://"))
					link = k[begLink : endLink]
					resStr.append(link)  # link

				begTitle = k.find("<strong>")
				if begTitle != (-1):
					tmpLen = len("<strong>")
					title = k[begTitle + tmpLen : len(k) - tmpLen]
					resStr.append(title)  # title or price


				if imgUrl is None and link is None and title is not None:
					endPrice = title.find("грн.")
					if endPrice != (-1):
						tmpStr = title[:endPrice]
						tmpStr1 = tmpStr.replace(' ', '')
						price = float(tmpStr1)  # formated price

						if len(resStr) == 4:
							resStr[3] = price

							# create dict
							for i in range(len(resStr)):
								resDict.update({ keysList[i]: resStr[i]})
							resDictList.append(dict(resDict))  # hard copy of dict obj
							numberOfElem+=1
						else:
							resStr.clear()

		# print(self.toJson({"result": resDictList}))
		return self.toJson({"result": resDictList})

	def toJson(self, data = None):
		if data is not None:
			# data = {}
			# data['key'] = 'value'
			json_data = json.dumps(data)
		else:
			print("toJson:", "Error: wrong data!")

		return json_data
						