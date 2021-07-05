#9.17  Построить треугольник, вписанный в окружность радиуса R.
from PIL import Image, ImageGrab, ImageFont, ImageDraw
R = int(input("Enter Radius:"))
img = Image.new("RGB", (R, R), (290, 290, 290))
draw = ImageDraw.Draw(img)
draw.arc((10, 10, R, R), 0, 360, fill=(0, 0, 0))
draw.polygon((0, R, R, R/3, R/3, R), fill=(255, 0, 0), outline=(0, 0, 0))
img.show()
