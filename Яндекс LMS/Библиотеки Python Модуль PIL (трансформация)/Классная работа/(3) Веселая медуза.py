from PIL import Image

rf, gf, bf = float(input()), float(input()), float(input())
im = Image.open("jellyfish.png")
width, height = im.size
pixels = im.load()

for x in range(width):
    for y in range(height):
        r, g, b = pixels[x, y]
        color = int(r * rf + g * gf + b * bf)
        pixels[x, y] = color, color, color
im.save("gray_jelly.png")
