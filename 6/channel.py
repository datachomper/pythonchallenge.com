import zipfile
import re

s = re.compile("\d+$")
file = open('channel.zip')
zip = zipfile.ZipFile(file)
dir = zip.infolist()

start = '90052'
out = ""

for f in dir:
	hurp = zip.read(start+".txt")
	out += zip.getinfo(start+".txt").comment
	m = s.search(hurp)
	print out
	start = m.group()
