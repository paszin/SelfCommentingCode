from HTMLParser import HTMLParser
import requests

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):

	found = False
	answer = ''
	def handle_starttag(self, tag, attrs):
		if tag == "a":
			self.found = True


	def handle_data(self, data):
		if self.found and not self.answer:
			self.answer = data


def getRandomExcuse():
	html = requests.get("http://programmingexcuses.com/").text
	parser = MyHTMLParser()
	parser.feed(html)
	return parser.answer

if __name__ == '__main__':
	# instantiate the parser and fed it some HTML
	parser = MyHTMLParser()
	parser.feed(u'<!DOCTYPE HTML>\n<html>\n<head>\n <title>Excuses For Lazy Coders</title>\n <meta name="keywords" content="Programming, Programmer, Devloping, Developer, Coding, Coders, Excuses, Reasons, Lies, Fibs, Blame, Justifications" />\n <meta name="description" content="Excuses For Lazy Coders" />\n <link rel="canonical" href="http://programmingexcuses.com/" />\n <style type="text/css">* {margin: 0;} html, body {height: 100%;} .wrapper {min-height: 100%; height: auto !important; height: 100%; margin: 0 auto -8em;} .footer, .push {height: 8em;}</style>\n</head>\n<body>\n <div class="wrapper">\n  <center style="color: 333; padding-top: 200px; font-family: Courier; font-size: 24px; font-weight: bold;"><a href="/" rel="nofollow" style="text-decoration: none; color: 333;">It was working in my head</a></center>\n  <div class="push"></div>\n </div>\n <div class="footer">\n  <center style="color: #333; font-family: Courier; font-size: 11px;">\n   <script type="text/javascript"><!--\n    google_ad_client = "ca-pub-4336860580083128";\n    google_ad_slot = "1671975908";\n    google_ad_width = 728;\n    google_ad_height = 90;\n    //-->\n   </script>\n   <script type="text/javascript" src="http://pagead2.googlesyndication.com/pagead/show_ads.js"></script>\n   <br /><br />&copy; Copyright 2012 - 2016 programmingexcuses.com - All Rights Reserved\n  </center>\n </div>\n <script type="text/javascript">\n  var _gaq = _gaq || [];\n  _gaq.push([\'_setAccount\', \'UA-33167244-1\']);\n  _gaq.push([\'_setDomainName\', \'programmingexcuses.com\']);\n  _gaq.push([\'_setAllowLinker\', true]);\n  _gaq.push([\'_trackPageview\']);\n  (function() {\n   var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n   ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n   var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n  })();\n </script>\n</body>\n</html>')
	print parser.answer