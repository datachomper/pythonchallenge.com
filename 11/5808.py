import Image

img = Image.open("cave.jpg")
odd = Image.new("RGBA", (640,480), "#000")
even = Image.new("RGBA", (640,480), "#000")
xx = yy = 0
for y in range(0, img.size[1]):
	for x in range(0, img.size[0]):
		p = img.getpixel((x,y))
		if (x+y) % 2 == 0: # Even
			even.putpixel((xx,yy),p)	
		else: # Odd
			odd.putpixel((xx,yy),p)	
		xx += 1
	xx = 0
	yy += 1
yy = 0
even.show()
odd.show()
