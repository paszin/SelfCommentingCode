

import re
import random
import os
import json

class TheEasyPlusRule:

	@classmethod
	def getComment(self, line):
		return "#This line uses the famous + operator"

	@classmethod
	def isMatching(self, line):
		return '+' in line


class StackOverflowCommentary
	@classmethod
	def getComment(self, line):
		json_string = "".join(os.popen('googler %s -j -w stackoverflow.com --json' % line))
		parsed = json.loads(json_string)
		abstract = parsed[0]['abstract']
		link = parsed[0]['url']
		return "{abstract}\n Please see SO link below for further information: \n{link}".format()

	@classmethod
	def isMatching(self, line):
		return line(len) > 100

