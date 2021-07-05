from PIL import Image, ImageGrab, ImageFont, ImageDraw
txt = Image.open("screen.png")
fnt = ImageFont.truetype("arial.ttf", 36)
d = ImageDraw.Draw(txt)
d.text((740, 430), 'hello world', font=fnt, fill=('#1f6992'))  # значения "740"
txt.save("file.png", "PNG")