

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
	def getComment(self, line):
		return "#This line uses the famous + operator"

	@classmethod
	def isMatching(self, line):
		return '+' in line

class StackOverflowCommentary:
	@classmethod
	def getComment(self, line):
		json_string = "".join(os.popen('googler %s -j -w stackoverflow.com --json' % line))
		parsed = json.loads(json_string)
		abstract = parsed[0]['abstract']
		link = parsed[0]['url']
		return "{abstract}\n Please see SO link below for further information: \n{link}".format(**locals())

	@classmethod
	def isMatching(self, line):
		return len(line) > 100


class HackerComments:
	@classmethod
	def getComment(self, line):
		return subprocess.Popen("ruby faker.rb", shell=True, stdout=subprocess.PIPE).stdout.read()

	@classmethod
	def isMatching(self, line):
		return len(line) > 10
