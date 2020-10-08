from scipy.spatial.distance import euclidean
import pickle
from PIL import Image
import math
from colorthief import ColorThief
import os
from time import sleep

def openSpritesPickle(fileName):
    # opens pickle file created in pokesprites.py.
    # this pickle file contains mean rgb colour values for each of the 151 sprites
    inFile = open(fileName, 'rb')
    sprites = pickle.load(inFile)
    inFile.close()
    return sprites

def getClosestSprite(pixel, spritesDict):
    # given mean colour of an area of picture, finds the euclidian distance between this & all sprites
    # returns the minimum euclidian distance, and returns that sprite
    closestSprite = min(spritesDict, key=lambda sprite : euclidean(spritesDict[sprite], pixel))
    return closestSprite

def getImageColour(imgObject):
    # gets mean colour of image object
    try:
        imgColour = imgObject.get_color(quality = 1)
        return imgColour
    except:
        return (0, 0, 0)

os.chdir(os.path.abspath(os.path.dirname(__file__)))

sprites = openSpritesPickle('sprites')

pixelScanSize = 8           # width/ height in pixels that will represent a single sprite.
spriteSize = 32             # pixel size of input sprites, (32x32 with pokemon sprites)

imgFileName = str(input('what is the name of your input image (with file extension)'))

img = Image.open(imgFileName)
width, height = img.size

newImg = img.crop((0,0,pixelScanSize,pixelScanSize))

outputImgHeight = divmod(height, pixelScanSize)[0] * spriteSize
outputImgWidth = divmod(width, pixelScanSize)[0] * spriteSize
outputImgSize = (outputImgWidth, outputImgHeight)
outputImg = Image.new('RGB', outputImgSize)

numIterations = (width/pixelScanSize) * (height/pixelScanSize)
curIteration = 0

# loop through width of image in chunks of pixels determined by pixel scan size
for w in range(math.floor(width/pixelScanSize)):
    # loop through height of image in chunks of pixels determined by pixel scan size
    for h in range(math.floor(height/pixelScanSize)):
        # creates new img object for area
        newImg=img.crop((w*pixelScanSize, h*pixelScanSize, w*pixelScanSize+pixelScanSize, h*pixelScanSize+pixelScanSize))
        # creates temp images from this image object for ColourThief to work with
        # program was failing here, adding multiple temp 'cache' images reduced failure rate
        # but did not completely stop it.
        # for rare cases when it still fails as temp images overlap, program will sleep for 0.5
        # seconds and try again
        while True:
            try:
                newImg.save(f'temp{curIteration % 2}.png')
                break
            except:
                sleep(0.5)
        imgObject = ColorThief(f'temp{curIteration % 2}.png')
        pixelColourTuple = getImageColour(imgObject)
        spriteName = getClosestSprite(pixelColourTuple, sprites)
        sprite = Image.open(f'pokesprites\\{spriteName}')
        outputImg.paste(sprite, (w * spriteSize, h * spriteSize))
        curIteration += 1
        print(f'{round((curIteration / numIterations) * 100, 2)}% complete')
        
outputImg.save(f'output{pixelScanSize}-{imgFileName}')
