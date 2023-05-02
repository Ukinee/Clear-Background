from PIL import Image
import glob

for image_path in glob.glob("Images/*.png"):
    img = Image.open(image_path)
    name = image_path.split("\\")[1]

    rgba = img.convert("RGBA")
    pixels = rgba.getdata()

    newPixels = []

    for pixel in pixels:
        if pixel[0] == 0 and pixel[1] == 255 and pixel[2] == 255:
            newPixels.append((255, 255, 255, 0))
        else:
            newPixels.append(pixel)

    rgba.putdata(newPixels)
    rgba.save("result/" + name, "PNG")
