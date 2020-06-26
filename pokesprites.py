from PIL import Image
import os
from colorthief import ColorThief
import pickle

# generates 

def pickleSpritesDict(fileName, spritesDict):
    outFile = open(fileName, 'wb')
    pickle.dump(spritesDict, outFile)
    outFile.close()

def getImageColour(imgObject):
    imgColour = imgObject.get_color(quality = 1)
    spritesDict[sprite] = imgColour
    return imgColour

if __name__ == '__main__':
    os.chdir(os.path.abspath(os.path.dirname(__file__)))
    spriteDir = f'{os.getcwd()}\\pokeSprites\\'

    spritesDict = {}

    for sprite in os.listdir(spriteDir):
        imgObject = ColorThief(f'pokeSprites\\{sprite}')
        getImageColour(imgObject)

    pickleSpritesDict('sprites', spritesDict)


