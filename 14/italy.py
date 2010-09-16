from PIL import Image

img = Image.open("wire.png")
new = Image.new("RGBA", (105,105))
red = Image.new("RGBA", (100,100))

z = 100
x = a = b = 0
try:
	while x < 10000:
		for a in range(100-z, z):
			p = img.getpixel((x, 0))
			new.putpixel((a,100-z),p)	
			x += 1
		for b in range(100-z, z-1):
			p = img.getpixel((x, 0))
			new.putpixel((z,b),p)	
			x += 1
		for a in range(z-1, 100-z, -1):
			p = img.getpixel((x, 0))
			new.putpixel((a,z),p)	
			x += 1
		for b in range(z, 100-z+2, -1):
			p = img.getpixel((x, 0))
			new.putpixel((100-z,b),p)	
			x += 1
		z -= 1

except:
	print "done!" # lol!
#new.save("cat", "png")

z = 0
for x in range(0,100):
	for y in range(0,100):
		p = img.getpixel((z,0))
		red.putpixel((x,y),p)
		z += 1	
red.save("red", "png")
