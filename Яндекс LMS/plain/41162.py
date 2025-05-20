from PIL import Image, ImageDraw

c = int(input())
left_color = input()
right_color = input()
space_between_lines = (250 - 60 * 2)
w, h = (400, 200 + 250 * c + space_between_lines * (c - 1))
image = Image.new("RGB", (w, h), "#777")
draw = ImageDraw.Draw(image)

for i in range(c):
    if i < c - 1:
        draw.arc(((w // 2 - 125, 100 + i * (250 + space_between_lines) + 190),
                  (w // 2 + 125, 100 + i * (250 + space_between_lines) + 250 + 190)), width=60, fill=right_color,
                 start=-90,
                 end=-270)
    draw.arc(((w // 2 - 125, 100 + i * (250 + space_between_lines)),
              (w // 2 + 125, 100 + i * (250 + space_between_lines) + 250)), width=60, fill=left_color, start=90,
             end=270)

image.save("colored_snake.png")
