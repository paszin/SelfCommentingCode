

import re
import random
import inspect
import sys
import os
import json
import subprocess

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
		return False ##skip for now
		libs = StackOverflowCommentary.getLibs(content)
		for lib in libs:
			if lib in line:
				return True

class HackerComments:
	@classmethod
	def getComment(self, line, content):
		return subprocess.Popen("ruby faker.rb", shell=True, stdout=subprocess.PIPE).stdout.read()

	@classmethod
	def isMatching(self, line, content):
		return '#' in line


class Todo:

	@classmethod
	def getComment(self, line, content):
		return "TODO: consider scenario where " + line.split(" ")[0] + "> 5"


	@classmethod
	def isMatching(self, line, content):
		return random.random() > 0.95

