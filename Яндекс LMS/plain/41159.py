from PIL import Image, ImageDraw

s = int(input())
width = 24 * s
height = 40 * s
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)
trunk_width = 3 * s
trunk_height = 4 * s

draw.polygon(((width / 2, 16 * s), (2 * s, 32 * s), (width - 2 * s, 32 * s)), fill="#00b050")
draw.polygon(((width / 2, 8 * s), (4 * s, 20 * s), (width - 4 * s, 20 * s)), fill="#00b050")
draw.polygon(((width / 2, 3 * s), (6 * s, 11 * s), (width - 6 * s, 11 * s)), fill="#00b050")

draw.rectangle((width / 2 - trunk_width / 2, 32 * s, width / 2 + trunk_width / 2, 36 * s), fill="#7f6000")

image.save("fir_tree.png")
