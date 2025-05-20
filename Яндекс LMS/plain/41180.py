from PIL import Image

c = int(input())
im = Image.open("book.png")
res = Image.new("RGB", (1000, 2000), "white")
y = 2000 - im.height
for i in range(c):
    res.paste(im, (1000 - im.width, y))
    im = im.resize((int(im.width * 0.9), int(im.height * 0.9)))
    y -= im.height
res.save("stack.png")
