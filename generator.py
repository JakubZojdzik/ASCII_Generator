from PIL import Image, ImageDraw, ImageFont

import math

chars = "#$@B*og?-_+:,\^`'. "
# chars = "#Wo- "[::-1]
charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 1


oneCharWidth = 5
oneCharHeight = 12

def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]

text_file = open("textOutput.txt", "w")

im = Image.open("input.jpg")

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor*height*(oneCharWidth/oneCharHeight))), Image.NEAREST)
im = im.convert('RGB')
width, height = im.size
pix = im.load()

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))

    text_file.write('\n')
