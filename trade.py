from PIL import Image
import glob

for image_path in glob.glob("C:/Users/xperi/Desktop/Python/Images/*.png"):
    img = Image.open(image_path)
    name = image_path.split("\\")[1]

    rgba = img.convert("RGBA")
    datas = rgba.getdata()

    newData = []

    for item in datas:
        if item[0] == 0 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    rgba.putdata(newData)
    rgba.save("result/" + name, "PNG")
