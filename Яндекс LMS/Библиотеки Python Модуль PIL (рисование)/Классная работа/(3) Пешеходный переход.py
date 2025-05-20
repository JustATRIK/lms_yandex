from PIL import Image, ImageDraw

w, h, s = map(int, input().split())
black_line_w = s // 4
image = Image.new("RGB", (w, h), "white")
draw = ImageDraw.Draw(image)

for i in range(w // (s + black_line_w)):
    if i % 2 != 0:
        draw.rectangle(((i * (s + black_line_w), 0), (i * (s + black_line_w) + s, h)), fill=(255, 192, 0))
    draw.rectangle(((i * (s + black_line_w) + s + 1, 0), (i * (s + black_line_w) + black_line_w + s - 1, h)),
                   fill="black")

image.save("crossing.png")
