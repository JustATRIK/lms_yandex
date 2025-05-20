from PIL import Image
from PIL.ImageDraw import ImageDraw

color = input()
im = Image.open("flowers.png")
width, height = im.size
draw = ImageDraw(im)

for i in range(width // 50):
    draw.rectangle(((50 * i, 480), (50 * i + 30, height)), fill=color)

im.save("fence.png")
