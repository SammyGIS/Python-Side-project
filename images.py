from PIL import Image, ImageFilter


img = Image.open(r"C:\Users\User\PycharmProjects\UdemyCompletePythonDeveloper-master\Sec.17 206 Images With Python\pikachu.jpg")

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur","png")

# try build grayscale images
img = Image.open(r"C:\Users\User\PycharmProjects\UdemyCompletePythonDeveloper-master\Sec.17 206 Images With Python\pikachu.jpg")

filtered_img = img.convert("L")
filtered_img.save("blur.png", "png")
# rotate images
crooked = filtered_img.rotate(90)

# resize image, the resize function only accepts a tupple
resize = filtered_img.resize((300,300))

# print image
#resize.show()

# crop pictures
box = (100,100,400,400)
region = filtered_img.crop(box)
region.save("region.png", "png")
region.show()

# reduce image to a small size thumbmail

image = Image.open(r"C:\Users\User\PycharmProjects\UdemyCompletePythonDeveloper-master\Sec.17 206 Images With Python\astro.jpg")

new_imag = image.resize((400,400))
new_imag.save("thumbnail.jpg")