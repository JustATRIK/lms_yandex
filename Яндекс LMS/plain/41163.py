from PIL import Image, ImageDraw

bgr_color = tuple(map(int, input().split()))
s = int(input())
w, h = (20 * s, 22 * s)
image = Image.new("RGB", (w, h), bgr_color)
draw = ImageDraw.Draw(image)

draw.ellipse(((s * 7, s * 7), (13 * s, 21 * s)), fill=(255, 250, 235))

draw.chord(((s * 3, s * 3), (17 * s, 17 * s)), fill=(192, 0, 0), start=180, end=360)

draw.rectangle(((s * 3, s * 20), (17 * s, 21 * s)), fill=bgr_color)

draw.rectangle(((s * 3, s * 19), (17 * s, 20 * s)), fill=(146, 208, 80))

draw.ellipse(((s * 9, s * 4), (11 * s, 6 * s)), fill=(255, 255, 255))
draw.ellipse(((s * 5, s * 7), (7 * s, 9 * s)), fill=(255, 255, 255))
draw.ellipse(((s * 13, s * 7), (15 * s, 9 * s)), fill=(255, 255, 255))


image.save("mushroom.png")
