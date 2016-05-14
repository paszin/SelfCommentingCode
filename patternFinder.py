

import re
import random


class TheEasyPlusRule:

	@classmethod
	def getComment(self, line):
		return "#This line uses the famous + operator"

	@classmethod
	def isMatching(self, line):
		return '+' in line
		
