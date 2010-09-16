file = open("evil2.gfx", "rb")

a = open("evila", "wb")
b = open("evilb", "wb")
c = open("evilc", "wb")
d = open("evild", "wb")
e = open("evile", "wb")

i = 0
byte = file.read(1)
while byte != "":
	if i == 0:
		a.write(byte)		
	elif i == 1:
		b.write(byte)
	elif i == 2:
		c.write(byte)
	elif i == 3:
		d.write(byte)
	elif i == 4:
		e.write(byte)
	i += 1;
	if i > 4:
		i = 0
	byte = file.read(1)
