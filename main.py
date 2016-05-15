
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
commentPrefix = '#&# '

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
					for rulec in patternFinder.getAllRules():
						rule = rulec(content, line.strip())
						if rule.isMatching():
							prefix = line.split(line.strip())[0] #code with indentation
							comment = rule.getComment()
							offset += 1
							if type(comment) == list:
								offset += (len(comment) - 2)
								comment = ('\n' + prefix + commentPrefix).join(comment)
							contentListNew.insert(i+offset-1, prefix + commentPrefix + comment)
				print('\n'.join(contentListNew))
			with open(os.path.join(dirpath, fn+".scc"), "w") as f:
				f.write('\n'.join(contentListNew))
