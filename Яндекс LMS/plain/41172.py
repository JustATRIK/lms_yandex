from PIL import Image

n = int(input())
im = Image.open("yoda.png")
width, height = im.size
pixels = im.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        max_dif = max(abs(r - g), abs(g - b), abs(r - b))
        pixels[x, y] = r + max_dif // n, g + max_dif // n, b + max_dif // n
im.save("sense.png")
