from PIL import Image, ImageDraw

w, h = map(int, input().split())
color = tuple(map(int, input().split()))
image = Image.new("RGB", (w, h), "white")
draw = ImageDraw.Draw(image)

for i in range(h // 2):
    draw.rectangle((0, i * 2, w, i * 2 + 2), fill=color)
    color = (min(255, color[0] + 2), min(255, color[1] + 2), min(255, color[2] + 2))

image.save("sunrise.png")
