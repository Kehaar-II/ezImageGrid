from PIL import Image
import sys
import os
import glob
from math import ceil, floor

supportedFormats = [".png", ".jpg", ".jpeg", ".gif", ".ppm", ".tiff", ".bmp", ".PNG", ".JPG", ".JPEG", ".GIF", ".PPM", ".TIFF", ".BMP"]
maxdigit = 4
desiredSize = [200, 300]
desiredRation = desiredSize[1] / desiredSize[0]

defaultWidth = 10
defaultSortMethode = "number"
defaultCentering = "none"

def cropImage(img):
    '''PIL.Image -> PIL.Image'''

    width, height = img.size
    ratio = height / width
    heightwiseCropAmount = (height - desiredSize[1]) / 2
    widthwiseCropAmount = (width - desiredSize[0]) / 2

    # image too tall, must use width as reference
    if ratio > desiredRation:
        img = img.resize((desiredSize[0], int(height / (width / desiredSize[0]))))
        if (width <= 0):
            return None
        img = img.crop((0, heightwiseCropAmount, width - widthwiseCropAmount, height - heightwiseCropAmount))
    # image too wide, must use height as reference
    else:
        img = img.resize((int(width / (height / desiredSize[1])), desiredSize[1]))
        if (width - widthwiseCropAmount <= widthwiseCropAmount):
            return None
        img = img.crop((widthwiseCropAmount, 0, width - widthwiseCropAmount, height - heightwiseCropAmount))

    return img

def assembleImages(imgs, width, center):
    '''PIL.Image[], int -> PIL.Image'''

    print("combining images")
    lenght = len(imgs)
    height = ceil(lenght / width)
    totalWidth, totalHeight = desiredSize[0] * width, desiredSize[1] * height
    img = Image.new(mode="RGB", size=(totalWidth, totalHeight), color = "white")
    img.paste((0, 0, 0), (0, 0, img.size[0], img.size[1]))
    currentWidth, currentHeight = 0, 0

    startsAt = 0
    endsAt = lenght
    gridSize = width * height
    if (center == "top" or center.startswith("both")):
        emptyCells = gridSize - lenght
        if (center == "both"):
            emptyCells = floor(emptyCells / 2)
        if (center == "both-bottom"):
            emptyCells = ceil(emptyCells / 2)
        currentWidth += int((desiredSize[0] * emptyCells) / 2)
        startsAt = int(gridSize / height - emptyCells)
        if (center.startswith("both")):
            endsAt = gridSize - width - emptyCells
        for i in range(startsAt):
            Image.Image.paste(img, imgs[i], (currentWidth, currentHeight))
            imgs[i].close
            currentWidth += desiredSize[0]
        currentWidth, currentHeight = 0, desiredSize[1]
    if (center == "bottom"):
        endsAt = gridSize - width

    for i in range(startsAt, endsAt):
        Image.Image.paste(img, imgs[i], (currentWidth, currentHeight))
        imgs[i].close
        currentWidth += desiredSize[0]
        if currentWidth > totalWidth - desiredSize[0]:
            currentWidth = 0
            currentHeight += desiredSize[1]

    if (center.startswith("both")  or center == "bottom"):
        emptyCells = gridSize - lenght
        if (center == "both"):
            emptyCells = ceil(emptyCells / 2)
        if (center == "both-bottom"):
            emptyCells = floor(emptyCells / 2)
        currentWidth += int((desiredSize[0] * emptyCells) / 2)
        for i in range(endsAt, lenght):
            Image.Image.paste(img, imgs[i], (currentWidth, currentHeight))
            imgs[i].close
            currentWidth += desiredSize[0]

    return img

def fileToCroppedImage(filepath):
    '''string -> PIL.Image'''
    return cropImage(Image.open(filepath))

def findImagesByDate(path):
    '''string -> PIL.Image[]'''
    files = list(filter(os.path.isfile, glob.glob(path + "*")))
    files.sort(key = lambda x: os.path.getmtime(x))
    out = []
    tmp = None

    for file in files:
        if (os.path.splitext(file)[1] in supportedFormats):
            print(file.rsplit('/', 1)[-1])
            tmp = fileToCroppedImage(file)
            if tmp != None:
                out.append(tmp)
    return out

def findImagesByName(path):
    '''string -> PIL.Image[]'''
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
                    tmp = fileToCroppedImage(currentfile)
                    if tmp != None:
                        list.append(tmp)
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
    '''string, bool -> PIL.Image[]'''
    print("images found:")
    if byDate:
        return findImagesByDate(path)
    else:
        return findImagesByName(path)

def printHelp():
    print(open("./help", "r").read().replace("%progName%", sys.argv[0]), end = '')

def isACTooSmall(ac, i):
    '''int, int -> bool'''
    if not ac in {4, 6, 8}:
        printHelp()
        return True
    return False

def verifyGeneralOptions(width__, sort__, center__, allOtherOptions):
    ''' '''
    allGeneralOptions = width__ + sort__ + center__
    av = sys.argv
    ac = len(av)

    width = defaultWidth
    sortMethode = defaultSortMethode
    center = defaultCentering

    generalOptionCount = 0

    for i in range(2, min(ac, 8), 2):
        if av[i] in allGeneralOptions:
            if i + 1 > ac - 1: # next > last index of av
                return None
            generalOptionCount += 1
        elif av[i] in allOtherOptions:
            break
        else:
            return None
        if av[i] in width__:
            if not av[i + 1].isnumeric():
                return None
            width = int(av[i + 1]) if int(av[i + 1]) >= 0 else width
        if av[i] in sort__:
            if not av[i + 1] in {"number", "date"}:
                return None
            sortMethode = av[i + 1]
        if av[i] in center__:
            if not av[i + 1] in {"top", "both", "both-bottom", "bottom"}:
                return None
            center = av[i + 1]
    return width, sortMethode, center, generalOptionCount

def verifyArgs():
    '''void -> string, int, String, String (width, sortMethode, center), [String]
    returns None, [error code], 0, 0, None on errors'''
    width__ = ["-w", "--width"]
    sort__ = ["-s", "--sort"]
    center__ = ["-c", "--center"]
    files__ = ["-f", "--files"]
    generalOptionCount = 0

    av = sys.argv
    ac = len(av)

    # no path
    if ac == 1:
        printHelp()
        return None, -1, 0, 0, None
    if av[1] == "-h" or av[1] == "--help":
        printHelp()
        return None, 0, 0, 0, None
    path = av[1] if av[1][-1] == '/' else av[1] + '/'

    # invalid path
    if ac >= 2 and not os.path.isdir(path):
        printHelp()
        return None, -2, 0, 0, None

    # only path
    if ac == 2:
        return path, defaultWidth, defaultSortMethode, defaultCentering, []

    tmp = verifyGeneralOptions(width__, sort__, center__, files__)
    if tmp == None:
        printHelp()
        return None, -3, 0, 0, None
    width, sortMethode, center, generalOptionCount = tmp

    # no further options
    if ac == 2 + generalOptionCount * 2:
        return path, width, sortMethode, center, []

    # arg is neither general nor other option
    if not av[2 + generalOptionCount * 2] in files__:
        return None, -4, 0, 0, None

    images = []
    for i in range(3 + generalOptionCount * 2, ac):
        file = path + av[i]
        if os.path.isfile(file):
            print(file)
            tmp = fileToCroppedImage(file)
            if tmp != None:
                images.append(tmp)
        else:
            print(av[i] + ": file not found")
    return path, width, sortMethode, center, images

def main():
    '''void -> int'''
    dir, width, sortMethode, center, images = verifyArgs()
    if dir == None:
        return 0 - width
    if len(images) == 0:
        images = findImages(dir, True if sortMethode == "date" else False)
    if images == None:
        return 100
    assembleImages(images, width, center).save(dir + "output.png")
    print("new image saved at " + dir + "output.png")
    return 0

exit(main())
