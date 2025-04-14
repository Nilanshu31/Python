from PIL import Image,ImageFilter,ImageDraw, ImageEnhance
#show
img = Image.open("ironman.jpg")
img.show()
#resize
size = (500,500)
img.thumbnail(size)
img.save('asdf.jpg')
img.show()
#filter
img_filtered = img.filter(ImageFilter.BLUR)
img_filtered.show("filtered_image.jpg")
#brightness
enhancer = ImageEnhance.Brightness(img)
img_bright = enhancer.enhance(1.8)
img_bright.show("bright_image.jpg")
#text
img = Image.open("asdf.jpg")
draw = ImageDraw.Draw(img)
draw.text((100,200),"Nilanshu")
img.show()
