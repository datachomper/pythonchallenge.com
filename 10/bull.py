# Classic Look-and-say sequence
# http://en.wikipedia.org/wiki/Look-and-say_sequence

seq = "11"

for x in range(1, 31):
	print "len(a[{0}])".format(x), "=", len(seq)
	tmp = ""
	run = 1
	last = seq[0]
	for i in range(0, len(seq)):
		if (i+1 != len(seq)) and (seq[i] == seq[i+1]):
			run += 1
		else:
			tmp += "{0}{1}".format(run, seq[i])
			run = 1
	seq = tmp
