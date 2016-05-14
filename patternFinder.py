

import re
import random
<<<<<<< HEAD
import inspect
import sys
import os
import json

def getAllRules():
    return [obj for name, obj in inspect.getmembers(sys.modules[__name__]) if inspect.isclass(obj)]
        
=======
import os
import json
>>>>>>> c7aeff97b776d7af16b7c80fe72036ad662b2e02

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
		return line(len) > 100

