

import re
import random
import inspect
import sys
import os
import json

def getAllRules():
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]
        

class TheEasyPlusRule:

	@classmethod
	def getComment(self, line, content):
		return "This line uses the famous + operator"

	@classmethod
	def isMatching(self, line, content):
		return '+' in line


class StackOverflowCommentary:

	@classmethod
	def getLibs(self, content):
		'''returns a list with names of used libaries'''
		libs = []
		for line in content.split('\n'):
			if line.startswith('import'):
				libs.append(line.split(' ')[1])
		return libs

	@classmethod
	def getComment(self, line, content=None):
		return "go to stackoverflow" ## replace this with stackoverflow call

	@classmethod
	def isMatching(self, line, content=None):
		libs = StackOverflowCommentary.getLibs(content)
		for lib in libs:
			if lib in line:
				return True
