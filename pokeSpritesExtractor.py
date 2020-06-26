# extracts individual 32x32 sprites from gen5icons-sheet spritesheet
# not needed to use program

import os
from PIL import Image

os.chdir(os.path.abspath(os.path.dirname(__file__)))

currentImg = 0

spriteSize = (32, 32) # (w, h)

spriteSheet = Image.open('gen5icons-sheet.png')
spriteSheetSize = spriteSheet.size

for a in range(int(spriteSheetSize[1] / spriteSize[1])):
    for b in range(int(spriteSheetSize[0] / spriteSize[0])):
        sprite = spriteSheet.crop((b * spriteSize[0], a * spriteSize[1], b * spriteSize[0] + spriteSize[0], a * spriteSize[1] + spriteSize[1]))
        whiteBGSprite = Image.new("RGB", sprite.size, "WHITE")
        whiteBGSprite.paste(sprite, (0, 0), sprite) 
        whiteBGSprite.save(f'{os.getcwd()}\\pokeSprites\\{currentImg}.png')
        currentImg += 1