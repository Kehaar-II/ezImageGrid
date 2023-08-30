from PIL import Image
import sys
import os
from math import ceil

supportedFormats = [".png", ".jpg", ".jpeg", ".gif", ".ppm", ".tiff", ".bmp", ".PNG", ".JPG", ".JPEG", ".GIF", ".PPM", ".TIFF", ".BMP"]
maxdigit = 4
desiredSize = [200, 300]
desiredRation = desiredSize[1] / desiredSize[0]

def cropImage(img):
    '''PIL image -> PIL image'''

    width, height = img.size
    ratio = height / width
    # image too tall, must use width as reference
    if ratio > desiredRation:
        img = img.resize((desiredSize[0], int(height / (width / desiredSize[0]))))
        cropAmount = (img.size[1] - desiredSize[1]) / 2
        img = img.crop((0, cropAmount, width, height - cropAmount))
    # image too wide, must use height as reference
    else:
        img = img.resize((int(width / (height / desiredSize[1])), desiredSize[1]))
        cropAmount = (img.size[0] - desiredSize[0]) / 2
        img = img.crop((cropAmount, 0 , width - cropAmount, height))
    return img

def assembleImages(imgs, width):
    '''PIL image list, int -> PIL image'''

    print("combining images")
    height = ceil(len(imgs) / width)
    totalWidth, totalHeight = desiredSize[0] * width, desiredSize[1] * height
    img = Image.new(mode="RGB", size=(totalWidth, totalHeight), color = "white")
    currentWidth, currentHeight = 0, 0

    for i in range(len(imgs)):
        Image.Image.paste(img, imgs[i], (currentWidth, currentHeight))
        imgs[i].close
        currentWidth += desiredSize[0]
        if currentWidth >= totalWidth:
            currentWidth = 0
            currentHeight += desiredSize[1]
    return img

def findImages(path):
    '''string -> int'''

    currentfile = None
    padding = ""
    hasFoundImageWithCurrentNb = True
    list = []

    print("images found:")
    i = 0
    while hasFoundImageWithCurrentNb or i <= 1:
        hasFoundImageWithCurrentNb = False
        for j in range(len(supportedFormats)):
            for k in range(maxdigit - (len(str(i)) - 1)):
                currentfile = path + padding + str(i) + supportedFormats[j]
                if os.path.isfile(currentfile):
                    print(currentfile.rsplit('/', 1)[-1])
                    list.append(cropImage(Image.open(currentfile)))
                    hasFoundImageWithCurrentNb = True
                padding += "0"
                if (hasFoundImageWithCurrentNb):
                    break
            padding = ""
            if (hasFoundImageWithCurrentNb):
                break
        i += 1
    if len(list) == 0:
        print("none")
        return None
    return list

def verifyArgs():
    '''void -> string, int
    returns None, [error code] on errors
    -1 = no arguments
    -2 = not a directory
    -3 = width not a number
    -4 = too many arguments'''

    av = sys.argv
    ac = len(av)

    if ac == 1:
        return None, -1
    path = av[1] if av[1][-1] == '/' else av[1] + '/'
    if ac >= 2 and not os.path.isdir(path):
        return None, -2
    if ac == 2:
        return path, 0
    if ac == 3:
        if not av[2].isnumeric():
            return None, -3
        elif int(av[2]) <= 0:
            return None, -3
        return path, int(av[2]) if int(av[2]) >= 0 else 0
    return None, -4

def main():
    '''void -> int'''

    dir, width = verifyArgs()

    if dir == None:
        return 0 - width
    images = findImages(dir)
    if images == None:
        return 5
    img = assembleImages(images, width if width > 0 else 10).save(dir + "output.png")
    print("new image saved at " + dir + "output.png")
    return 0

exit(main())
