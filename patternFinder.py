

import re
import random
import inspect
import sys


def getAllRules():
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]
        

class TheEasyPlusRule:

	@classmethod
	def getComment(self, line):
		return "#This line uses the famous + operator"

	@classmethod
	def isMatching(self, line):
		return '+' in line
		
