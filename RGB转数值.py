from PIL import Image
import math


f = open("2.txt", 'w+')  
im = Image.open('1.png')

width = im.size[0]
height = im.size[1]

rgb_im = im.convert('RGB')
for j in range(height):
        for i in range(width):
                r, g, b = rgb_im.getpixel((i, j))
                print(r, g, b,file=f)
