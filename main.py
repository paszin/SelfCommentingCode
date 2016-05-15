
## do this for compatibility with version 3
from __future__ import print_function

import os
import sys


import patternFinder

try:
	path = sys.argv[1]
except:
	path = "./example"

endings = ["py"]

for dirpath, dirnames, filenames in os.walk(path):
	for fn in filenames:
		if fn.split('.')[-1] in endings:
			print("Found File:", fn)
			with open(os.path.join(dirpath, fn)) as f:
				content = f.read()
				contentList = content.split('\n')
				contentListNew = contentList[:]
				for i, line in enumerate(contentList):
					for rule in patternFinder.getAllRules():
						if rule.isMatching(line, content):
							print(rule)
							comment = '#' + rule.getComment(line, content)
							contentListNew.insert(i, comment)
				print('\n'.join(contentListNew))
			with open(os.path.join(dirpath, fn+".scc"), "w") as f:
				f.write('\n'.join(contentListNew))
