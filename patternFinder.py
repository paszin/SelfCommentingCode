

import re
import random
import inspect
import sys
import os
import json
import subprocess
import urllib2
import requests
import so_helper
import phrases_pool as phrases


def getAllRules():
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]


class Rule:

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
		return "TODO: consider scenario where " + (self.line.replace('if', 'if ').split(" ")[1]).strip() + " > 5"


	def isMatching(self):
		return self.line.startswith('if')

class BuiltInExplain(Rule):

	keywords = ["range", "xrange", "map", "max", "min", "int", "len", "str", "abs"]

	def getComment(self):
		return " ".join([phrases.getRandomOpinion()+",", 
			"because", self.matchingKeyword, eval(self.matchingKeyword+'.__doc__').split('\n')[0]])

	def isMatching(self):
		for k in self.keywords:
			if k+'(' in self.line:
				self.matchingKeyword = k
				return True


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


