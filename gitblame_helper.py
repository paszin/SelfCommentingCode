import os

##b45d352d (Pascal            2016-05-14 15:39:14 -0700 40) for dirpath, dirnames, filenames in os.walk(path):

def blame(filename, line):
	repo_path = os.getcwd()
	fname = filename
	blame = []
	cmd = 'cd {path};git blame {fname}'.format( ## or --show-email
	            path=repo_path,
	            fname=fname)
	with os.popen(cmd) as process:
	   blame = process.readlines()
	resp = {}
	resp['name'] = extractName(blame[line])
	return resp


def extractName(text):
	i = text.find('(')
	j = text.find(' ', i)
	return text[i:j]


if __name__ == '__main__':
	print(blame(1, 1, 14))