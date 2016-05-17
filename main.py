
## do this for compatibility with version 3
from __future__ import print_function

import random
import os
import sys
import argparse

import patternFinder



## parse arguments
parser = argparse.ArgumentParser(description='this serious tool will make your code more readable, easier to understand and more fun to collaborate')
parser.add_argument('--path', metavar='P', type=str,
                   help='path to your codebase')
parser.add_argument('--newfile', action="store_true",
                   help='adds the comment to a new file')
parser.add_argument('--messup', action="store_true",
                   help='whatever')
parser.add_argument('--massivestackoverflow', action="store_true",
                   help='comments every line with a stackoverflow link')
#parser.add_argument('--savedb', action="store_true",
#                   help='save results to database')


args = parser.parse_args()
path = args.path
print(path)
path = "example"

endings = ["py"]
commentPrefix = '#&# '
noFrequency = True
newFile = False #args.newfile
onlyOneComment = True #args.messup

for dirpath, dirnames, filenames in os.walk(path):
	for fn in filenames:
		if fn.split('.')[-1] in endings:
			print("Found File:", fn)
			with open(os.path.join(dirpath, fn)) as f:
				content = f.read()
				contentList = content.split('\n')
				contentListNew = contentList[:]
				offset = 0
				for i, line in enumerate(contentList):
					allRules = patternFinder.getAllRules()
					random.shuffle(allRules)
					for rulec in allRules:
						rule = rulec(content, line.strip())
						if rule.isMatching() and (random.random() <= rule.frequency or noFrequency):
							prefix = line.split(line.strip())[0] #code with indentation
							try:
								comment = rule.getComment()
							except:
								continue
							offset += 1
							print(rule)
							if type(comment) == list:
								offset += (len(comment) - 2)
								comment = ('\n' + prefix + commentPrefix).join(comment)
							contentListNew.insert(i+offset-1, prefix + commentPrefix + comment)
							if onlyOneComment:
								break
				print('\n'.join(contentListNew))
				if newFile:
					ending = ".monty"
				else:
					ending = ""
			with open(os.path.join(dirpath, fn+ending), "w") as f:
				f.write('\n'.join(contentListNew))
