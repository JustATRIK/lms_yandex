from PIL import Image

color = input()
im = Image.open("yandex_logo.png")
width, height = im.size
pixels = im.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        if color == "red" and (r, g, b) == (0, 0, 0):
            pixels[x, y] = (255, 0, 0)
        elif color == "black" and (r, g, b) == (255, 0, 0):
            pixels[x, y] = (0, 0, 0)

im.save("ready.png")
