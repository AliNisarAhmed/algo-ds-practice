from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):

	@abstractmethod
	def __len__(self):
		"""Length of sequence"""

	@abstractmethod
	def __getitem__(self, j):
		"""get item at index j"""

	def __contains__(self, val):
		for j in range(len(self)):
			if self[j] == val:
				return True
		return False

	def index(self, val):
		for j in range(len(self)):
			if self[j] == val:
				return j
		raise ValueError('value not in sequence')


	def counts(self, val):
		k = 0
		for j in range(len(self)):
			if self[j] == val:
				k += 1
		return k

	def __eq__(self, other):
		if len(self) != len(other):
			return False
		for i in range(len(other)):
			if self[i] != other[i]:
				return False
		return True