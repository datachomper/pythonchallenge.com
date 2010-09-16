from PIL import Image

im = Image.open('oxygen.png')

ytop = xright = 0
while True:
	p = im.getpixel((0, ytop))
	if p[0] == p[1] == p[2]:
		break	
	ytop += 1
while True:
	p = im.getpixel((xright, ytop))
	if (p[0] != p[1]) or (p[1] != p[2]):
		break
	xright += 1

message = ""
last = 0
for col in range(0, xright):
	red = im.getpixel((col, ytop))[0]
	if last != red: 
		message += chr(red)
		last = red
print message
print len(message)

solution = [105, 110, 116, 101, 103, 114, 105, 116, 121]
final = ""
for x in solution:
#	final += chr(im.getpixel((x, ytop))[0])
#	print im.getpixel((x, ytop))
	final += chr(x)
print final
