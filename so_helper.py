

def getSOUrl(q):
	url = 'https://api.stackexchange.com/2.2/search/advanced?'
	key = 'uoLsU1Zq)G64b)a7Z9opVg(('
	site = 'stackoverflow'
	#order=desc&sort=activity&
	q=q.replace(" ", '%20')
	tagged = 'python'
	return url + '&'.join([k+'='+v for k, v in {'key': key, 'site': site, 'q': q, 'tagged': tagged}.items()])	