from PIL import Image
from PIL.Image import Transpose

coords = tuple(map(int, input().split()))
reflect = input() == "reflect"
im = Image.open("desert.png")
width, height = im.size

camel = Image.open("camel.png")
if reflect:
    camel = camel.transpose(method=Transpose.FLIP_LEFT_RIGHT)
im.paste(camel.copy(), (coords[0], coords[1]))

im.save("happy_camel.png")
