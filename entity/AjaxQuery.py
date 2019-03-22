from flask import request
class AjaxQuery:
	def __init__(self):
		self.query_string = ""
		self.page_num = 1
		self.only_with_photo = False
		self.only_with_delivery = False
		self.filter_money_from = 0
		self.filter_money_to = 9999999999

		# I dont know how many lvls exists in olx
		self.categories_lvls = []

		self.currency = ""
		self.order_by = "created_at%30Adesc"
		self.dist = ""

		self.init_props(request.args.to_dict())

		pass

		def init_props(self, args):
			# Init self properties from request args
			for prop in self.__dict__:
				if args[prop] is not None:
					self.query_string = args[prop]
			pass
	pass