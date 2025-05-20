from PIL import Image

n = map(int, input())
im = Image.open("fruits.png")
width, height = im.size
coords = [(0, 0, width // 2, height // 2), (width // 2, 0, width, height // 2),
          (0, height // 2, width // 2, height), (width // 2, height // 2, width, height)]
fruits = [im.crop(box) for box in coords]

for i, v in enumerate(n):
    im.paste(fruits[v - 1], coords[i])
im.save("cycle.png")
