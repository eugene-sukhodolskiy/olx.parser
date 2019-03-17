import requests

class Parser:
	_keyWord = None

	def __init__(self):
		pass

	def keyWord(self, word = None):
		self._keyWord = word
		# print(self._keyWord)

	def hi(self):
		greetings = "HI "
		# print(self._keyWord)
		if self._keyWord is not None:
			greetings += str(self._keyWord) + " "
		return greetings[:-1]

	def resp(self):
		response = requests.get('https://www.olx.ua//list/q-samsung/')
		a = str(response.content)
		b = a.split("class=\"wrap\"")
		for i in b:
			l = i.split(">\\n")
			for k in l:
				subStr = "<img class=\"fleft\" src=\""
				begSrc = k.find(subStr)
				if begSrc != (-1):
					begSrc+=len(subStr)
					endSrc = k.find("\"", begSrc + 1)
					# print(k[begSrc : endSrc])
					# print("___________________________")