from PIL import Image

angle = int(input())
color = tuple(map(int, input().split(", ")))
im = Image.open("sunflower.png")
width, height = im.size

pixels = im.load()
targ_color = pixels[0, 0]

im = im.rotate(angle=angle)
pixels = im.load()

for x in range(width):
    for y in range(height):
        if pixels[x, y] == (0, 0, 0) or pixels[x, y] == targ_color:
            pixels[x, y] = color

im.save("turned_sunflower.png")
