from scipy.spatial.distance import euclidean
import pickle
from PIL import Image
import math
from colorthief import ColorThief
import os

def openSpritesPickle(fileName):
    inFile = open(fileName, 'rb')
    sprites = pickle.load(inFile)
    inFile.close()
    return sprites

def getClosestSprite(pixel, spritesDict):
    closestSprite = min(spritesDict, key=lambda sprite : euclidean(spritesDict[sprite], pixel))
    return closestSprite

def getImageColour(imgObject):
    imgColour = imgObject.get_color(quality = 1)
    return imgColour

os.chdir(os.path.abspath(os.path.dirname(__file__)))

sprites = openSpritesPickle('sprites')

# pixel = (85, 205, 252)
# print(getClosestSprite(pixel, sprites))
img = Image.open('testimg.png')
width, height = img.size
width, height = 201, 201

newImg = img.crop((0,0,16,16))
print(newImg.size)

outputImgHeight = divmod(height, 16)[0] * 16
outputImgWidth = divmod(width, 16)[0] * 16
outputImgSize = (outputImgWidth, outputImgHeight)
outputImg = Image.new('RGB', outputImgSize)

for w in range(math.floor(width/16)):
    for h in range(math.floor(height/16)):
        newImg=img.crop((w*16, h*16, w*16+16, h*16+16))
        newImg.save('temp.png')
        imgObject = ColorThief(f'temp.png')
        spriteName = getClosestSprite(getImageColour(imgObject), sprites)
        sprite = Image.open(f'pokesprites\\{spriteName}')
        outputImg.paste(sprite, (w, h))
        outputImg.save('outputimg.png')