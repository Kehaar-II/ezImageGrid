from PIL import Image
import sys
import os
from math import ceil

supportedFormats = [".png", ".jpg", ".jpeg", ".gif", ".ppm", ".tiff", ".bmp", ".PNG", ".JPG", ".JPEG", ".GIF", ".PPM", ".TIFF", ".BMP"]
maxdigit = 4
imageSize = [200, 300]

def cropImage(img):
    '''PIL image -> PIL image'''

    width, height = img.size
    ratio = 1
    if height > width:
        ratio = height / imageSize[1]
    else:
        ratio = width / imageSize[0]
    img = img.resize((int(width / ratio), int(height / ratio)))

    return img

def assembleImages(imgs, width):
    '''PIL image list, int -> PIL image'''

    print("combining images")
    height = ceil(len(imgs) / width)
    totalWidth, totalHeight = imageSize[0] * width, imageSize[1] * height
    img = Image.new(mode="RGB", size=(totalWidth, totalHeight), color = "white")
    currentWidth, currentHeight = 0, 0

    for i in range(len(imgs)):
        Image.Image.paste(img, imgs[i], (currentWidth, currentHeight))
        currentWidth += imageSize[0]
        if currentWidth >= totalWidth:
            currentWidth = 0
            currentHeight += imageSize[1]
    img.show()

    return 0

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
                    list.append(cropImage(Image.open(currentfile)))
                    print(currentfile.rsplit('/', 1)[-1])
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
    assembleImages(images, width if width > 0 else 10)

    return 0

exit(main())
