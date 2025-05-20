from PIL import Image

s = int(input())
size = s - s // 5
im = Image.open("ornament.png")
im = im.resize((size, size))
res = Image.new("RGB", (s, s), "#208d80")
res.paste(im, (s // 10, s // 10))
res.save("tile.png")
