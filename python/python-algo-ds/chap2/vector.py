if __name__="__main__":
	class Vector:
		def __init__(self, d):
			if isinstance(d, int):
				self._coords = [0] * d
			elif isinstance(d, list):
				coords = []
				for i in range(len(d)):
					coords[i] = d[i]
				self._coords = coords

		def __len__(self):
			return len(self._coords)

		def __getitem__(self, j):
			return self._coords[j]

		def __setitem__(self, j , val):
			self._coords[j] = val

		def __add__(self, other):
			if len(self) != len(other):
				raise ValueError("dimensions must agree")
			result = Vector(len(self))
			for j in range(len(self)):
				result[j] = self[j] + other[j]
			return result

		def __radd__(self, other):
			return self.__add__(other);

		def __mul__(self, m):
			result = Vector(len(self))
			for i in range(len(self)):
				result[i] = self[i] * m
			return result

		def __sub__(self, other):
			if len(self) != len(other):
				raise ValueError('dimensions must agree')
			result = Vector(len(self))
			for j in range(len(self)):
				result[j] = self[j] - other[j]
			return result

		def __neg__(self):
			result = Vector(len(self))
			for i in range(len(self)):
				result[i] = -1 * self[j]
			return result

		def __eq__(self, other):
			return self._coords == other._coords

		def __ne__(self, other):
			""" Returns true if vector differs from other"""
			return not self == other

		def __str__(self):
			return '<' + str(self._coords)[1: -1] + '>'
