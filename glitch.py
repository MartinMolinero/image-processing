import random
from PIL import Image
from PIL import ImageFilter

def pointillism(input_filename, output_filename):
    im = Image.open(input_filename)

    pixels = im.load()

    for i in range(im.width):
        for j in range(im.height):
            prob = random.random()
            if prob <= 0.3:
                pixels[i, j] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))  # set pixel to red
            elif prob < 0.6 and prob > 0.3:
                pixels[i, j] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))  # set pixel to red

    im.save(output_filename)

def reduce_noise(input_filename):
    im = Image.open(input_filename)
    im1 = im.filter(ImageFilter.BLUR)
    im2 = im.filter(ImageFilter.MinFilter(3))
    im3 = im.filter(ImageFilter.MinFilter)
    im1.save('im1.jpeg')
    im2.save('im2.jpeg')
    im3.save('im3.jpeg')