import urllib
import re

p = re.compile('\d+$')
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
nothing = "46059"

for i in range(1, 400):
	page = urllib.urlopen(url+nothing)
	txt = page.read()
	print txt
	m = p.search(txt)
	nothing = m.group()
