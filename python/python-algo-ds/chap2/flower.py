class Flower:
	def __init__(self, name = "Anonymous", petals = 3, price = 0.0):
		self._name = name
		self._petals = petals
		self._price = price

	def get_name(self):
		return self._name

	def set_name(self, val):
		self._name = val
		return self

	def get_petals(self):
		return self._petals

	def set_petals(self, val):
		self._petals = val
		return self

	def get_price(self):
		return self._price

	def set_price(self, val):
		self._price = val
		return self