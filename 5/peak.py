import pickle, pprint

f = open('banner.p', 'rb')
p = pickle.load(f)

for row in p:
	r = ""
	for col in row:
#		print "got {0} for {1} spaces".format(col[0], col[1])
		for s in range(col[1]):
			r += "{0}".format(col[0])
	print r
