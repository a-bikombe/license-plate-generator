#!/usr/bin/env python3

import random

class LicensePlate:

	def __init__(self):
		self.plate = []

	def standard(self):
		for place in range(7):
			self.plate.append(random.randrange(10))
		return self.plate

	def alphanumeric(self):
		for place in range(7):
			self.plate.append(random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
		return self.plate
		
person_a = LicensePlate()
print(person_a.standard())
person_b = LicensePlate()
print(person_b.alphanumeric())