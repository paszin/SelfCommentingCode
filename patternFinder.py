

import re
import random
import math
import inspect
import sys
import os
import json
import subprocess
import requests
import so_helper
import phrases_pool as phrases


def getAllRules():
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]


class Rule:
	'''Basic Class, all Rules are inherited from this''' 

	def __init__(self, content, line):
		self.content = content
		self.line = line

	def isMatching(self):
		return False

	def getComment(self):
		return ''


class TheEasyPlusRule(Rule):
	
	def getComment(self ):
		return "This line uses the famous + operator"

	
	def isMatching(self ):
		return '+' in self.line

class StackOverflowCommentary(Rule):

	def getLibs(self):
		'''returns a list with names of used libaries'''
		libs = []
		for line in self.content.split('\n'):
			if line.startswith('import'):
				libs.append(line.split(' ')[1])
		return libs

	
	def getComment(self):
		return "Placeholder for SO link" ## save some time
		q = self.lib + " bug" 
		url = so_helper.getSOUrl(q)
		print(url)
		data = requests.get(url).json()
		#print(data['items'][0])
		return str(data['items'][0][u'title']) + '\n#' + "Details: " + "http://stackoverflow.com/questions/" + str(data['items'][0]['question_id'])
	
	
	def isMatching(self):
		libs = self.getLibs()
		for lib in libs:
			if lib in self.line: # and random.random() > 0.5:
				self.lib = lib
				return True


class HackerComments(Rule):
	
	def getComment(self):
		comment = subprocess.Popen("ruby faker.rb", shell=True, stdout=subprocess.PIPE).stdout.read()
		return comment.split('\n')
	
	def isMatching(self):
		return '#' in self.line

class Todo(Rule):

	def getComment(self):
		return "TODO: consider scenario where " + (self.line.replace('if', 'if ').replace(2*' ', ' ').split(" ")[1]).strip() + " > 5"


	def isMatching(self):
		return self.line.startswith('if')

class BuiltInExplain(Rule):

	keywords = ["range", "xrange", "map", "max", "min", "int", "len", "str", "abs", "enumerate", "buffer"]

	def getComment(self):
		return " ".join([phrases.getRandomOpinion()+",", 
			"because", self.matchingKeyword, eval(self.matchingKeyword+'.__doc__').split('\n')[0]]).replace(self.matchingKeyword + ' ' + self.matchingKeyword, self.matchingKeyword)

	def isMatching(self):
		for k in self.keywords:
			if k+'(' in self.line:
				self.matchingKeyword = k
				return True


class FixMe(Rule):

	def getComment(self):
		bugUrl = "https://bugs.python.org/issue" + str(int(random.random()*10**5))
		return "Fix: " + "This bahavoir is because of " + bugUrl

	def isMatching(self):
		return self.line.count('.') > 2

class DoNotToucht(Rule):

	def getComment(self):
		return "!DO NOT TOUCH!"

	def isMatching(self):
		return len(self.line) > 80


class Meaning(Rule):

	def getComment(self):
		name, value = self.line.split('=')
		try:
			float(value)
		except:
			return name + 'stores the state of the process'
		else:
			return name + 'is ' + value + ' but it could also be ' + str(round(float(value)*random.random()*2, 3)) + ' or ' + str(round(float(value)*random.random()*80, 1))

	def isMatching(self):
		return '=' in self.line and '+' not in self.line and '-' not in self.line and len(self.line.split('=')) == 2


class NumberFacts(Rule):

	def getComment(self):
		return requests.get("http://numbersapi.com/{number}/math".format(number=self.number)).text

	def isMatching(self):
		numbers = [int(s) for s in self.line.split() if s.isdigit()]
		if numbers:
			self.number = random.choice(numbers)
			return True
		return False


if __name__ == '__main__':
	print("Test Patterns")
	content = '''import sys
	sys.argv
	abs(-4)'''
	s = StackOverflowCommentary('sys.argv', 'import sys')
	if s.isMatching(): 
		print(s.isMatching(), s.lib)
		print(s.getComment())

	r = HackerComments(content, "#")
	print(r.getComment())

	r = FixMe('', '...')
	print(r.isMatching(), r.getComment())

	r = Meaning('', 'c = 4')
	print(r.isMatching(), r.getComment())

	r = NumberFacts('', 'c = 4')
	print(r.isMatching(), r.getComment())






