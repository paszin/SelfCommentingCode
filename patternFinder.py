

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
import gitblame_helper
import programmingexcuses as excuses


def getAllRules():
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]


class Rule:
	'''Basic Class, all Rules are inherited from this'''

	frequency = 0.5 #add some randomness

	def __init__(self, content, line):
		self.content = content
		self.line = line

	def isMatching(self):
		return False

	def getComment(self):
		return ''


class ExplainTheBasics(Rule):
	'''when a line contains a plus, explain how awesome this is'''

	frequency = 0.4

	def getComment(self):
		return "This line uses the {what} + operator".format(what=phrases.getRandomAdjective())

	def isMatching(self):
		return '+' in self.line and '+=' not in self.line



class StackOverflowCommentary(Rule):

	frequency = 0.3

	def getLibs(self):
		'''returns a list with names of used libaries'''
		libs = []
		for line in self.content.split('\n'):
			if line.startswith('import'):
				libs.append(line.split(' ')[1])
		return libs


	def getComment(self):
		#return "Placeholder for SO link" ## save some time
		q = self.lib + random.choice([" bug", " problem", " help"])
		url = so_helper.getSOUrl(q)
		#print(url)
		data = requests.get(url).json()
		question = random.choice(data['items'])
		#print(data['items'][0])
		return [str(question[u'title']), "For more details go to " + "http://stackoverflow.com/questions/" + str(question['question_id'])]


	def isMatching(self):
		libs = self.getLibs()
		for lib in libs:
			if lib in self.line and "import" not in self.line: # and random.random() > 0.5:
				self.lib = lib
				return True


class HackerComments(Rule):

	frequency = 1

	def getComment(self):
		return phrases.getRandomHackerComment() #subprocess.Popen("ruby faker.rb", shell=True, stdout=subprocess.PIPE).stdout.read()

	def isMatching(self):
		return '#' in self.line and '#&#' not in self.line or "import" in self.line

class Todo(Rule):

	frequency = 0.7

	def getComment(self):
		return "TODO: consider scenario where " + (self.line.replace('if', 'if ').replace(2*' ', ' ').split(" ")[1]).strip() + " > " + str(random.randrange(10))

	def isMatching(self):
		return self.line.startswith('if')

class BuiltInExplain(Rule):

	frequency = 0.5

	keywords = ["range", "xrange", "map", "max", "min", " int", "len", "str", "abs", "enumerate", "buffer", "filter"]

	def getComment(self):
		return " ".join([phrases.getRandomOpinion()+",",
			"because",
			self.matchingKeyword,
			eval(self.matchingKeyword+'.__doc__').split('\n')[0]]).replace(self.matchingKeyword + ' ' + self.matchingKeyword, self.matchingKeyword)

	def isMatching(self):
		for k in self.keywords:
			if k+'(' in self.line:
				self.matchingKeyword = k
				return True


class FixMe(Rule):

	def getComment(self):
		bugUrl = "https://bugs.python.org/issue" + str(int(random.random()*10**5))
		return "Fix: " + "This behavoir is because of " + bugUrl

	def isMatching(self):
		return self.line.count('.') > 2

class DoNotToucht(Rule):

	def getComment(self):
		return "!DO NOT TOUCH! Crucial to Thread Locking"

	def isMatching(self):
		return len(self.line) > 80


class Meaning(Rule):

	def getComment(self):
		name, value = self.line.split('=')
		try:
			float(value)
		except:
			return name + ' ' + phrases.getRandomMeaning()
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

class Excuses(Rule):

	def getComment(self):
		return str(excuses.getRandomExcuse())

	def isMatching(self):
		return 'print' in self.line or "debug" in self.line.lower()

class CopyCode(Rule):

	def getComment(self):
		return "This code is copied from " + so_helper.getSOUrl(random.choice(["function", "recursion"]))

	def isMatching(self):
		return self.line.startswith("def")

class GitBlame(Rule):


	def getComment(self):
		pass
		#i = self.content.splitlines().index(self.line)
		#gitblame_helper.blame(i)

	def isMatching(self):
		return False #self.content.count(self.line) > 1 and self.line.strip()


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

	r = Excuses('', 'print("hello")')
	print(r.isMatching(), r.getComment())






