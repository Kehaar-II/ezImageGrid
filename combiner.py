from PIL import Image
import sys
import os
import glob
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
        if (width <= 0):
            return None
        img = img.crop((0, cropAmount, width, height - cropAmount))
    # image too wide, must use height as reference
    else:
        img = img.resize((int(width / (height / desiredSize[1])), desiredSize[1]))
        cropAmount = (img.size[0] - desiredSize[0]) / 2
        if (width - cropAmount <= cropAmount):
            return None
        img = img.crop((cropAmount, 0 , width - cropAmount, height))
    return img

def assembleImages(imgs, width, center):
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

def findImagesByDate(path):
    '''string -> PIL image list'''
    files = list(filter(os.path.isfile, glob.glob(path + "*")))
    files.sort(key = lambda x: os.path.getmtime(x))
    out = []
    tmp = None

    for file in files:
        if (os.path.splitext(file)[1] in supportedFormats):
            print(file.rsplit('/', 1)[-1])
            tmp = cropImage(Image.open(file))
            if tmp != None:
                out.append(tmp)
    return out

def findImagesByName(path):
    '''string -> PIL image list'''
    currentfile = None
    padding = ""
    hasFoundImageWithCurrentNb = True
    list = []

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

def findImages(path, byDate):
    '''string, bool -> string[]'''
    print("images found:")
    if byDate:
        return findImagesByDate(path)
    else:
        return findImagesByName(path)


def printHelp():
    print(open("./help", "r").read().replace("%progName%", sys.argv[0]))
    return

def verifyArgs():
    '''void -> string, int, String, String (width, sortMethode, center)
    returns None, [error code], 0, 0 on errors
    -1 = no arguments
    -2 = not a directory
    -3 = width not a number
    -4 = too many arguments'''

    width = 10
    sortMethode = "number"
    center = "none"

    av = sys.argv
    ac = len(av)

    if ac == 1: # no path
        printHelp()
        return None, -1, 0, 0

    if av[1] == "-h" or av[1] == "--help":
        printHelp()
        return None, 0, 0, 0

    path = av[1] if av[1][-1] == '/' else av[1] + '/'
    if ac >= 2 and not os.path.isdir(path): # invalid path
        printHelp()
        return None, -2, 0, 0
    if ac == 2: # only path
        return path, width, sortMethode, center
    if (ac % 2) != 0: # one of the options is wrong, don't need to check any further, may need to remove if adding support for giving files directly from the command
        printHelp()
        return None, -5, 0, 0

    for i in range(2, ac, 2):
        if av[i] in {"-w", "--width"}:
            if not av[i + 1].isnumeric():
                return None -3, 0, 0
            width = int(av[i + 1]) if int(av[i + 1]) >= 0 else width
        if av[i] in {"-s", "--sort"}:
            if not av[i + 1] in {"number", "date"}:
                return None, -6, 0, 0
            sortMethode = av[i + 1]
        if av[i] in {"-c", "--center"}:
            if not av[i + 1] in {"top", "bottom", "both"}:
                return None, -7, 0, 0
            center = av[i + 1]
    return path, width, sortMethode, center

def main():
    '''void -> int'''

    dir, width, sortMethode, center = verifyArgs()

    if dir == None:
        return 0 - width
    images = findImages(dir, True if sortMethode == "date" else False)
    if images == None:
        return 5
    assembleImages(images, width, center).save(dir + "output.png")
    print("new image saved at " + dir + "output.png")
    return 0

exit(main())
