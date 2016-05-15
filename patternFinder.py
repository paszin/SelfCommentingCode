

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
		libs = StackOverflowCommentary.getLibs(content)
		for lib in libs:
			if lib in line:
				q = lib + " bug" 
		url = so_helper.getSOUrl(q)
		print(url)
		data = requests.get(url).json()
		#print(data['items'][0])
		return str(data['items'][0][u'title']) + '\n#' + "Details: " + "http://stackoverflow.com/questions/" + str(data['items'][0]['question_id'])
	
	@classmethod
	def isMatching(self, line, content=None):
		libs = StackOverflowCommentary.getLibs(content)
		for lib in libs:
			if lib in line and random.random() > 0.5:
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
		return "TODO: consider scenario where " + (line.split(" ")[0]).strip() + " > 5"


	@classmethod
	def isMatching(self, line, content):
		return random.random() > 0.95



if __name__ == '__main__':
	print(StackOverflowCommentary.getComment('sys.argv', 'import sys'))


