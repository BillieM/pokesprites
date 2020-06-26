*WARNING, CODE IS MESSY & UNOPTIMISED* 
-------------------------------------------------------------------------------------------------------------------------------------

This script is used for generating collages using sprites of the original 151 pokemon (using gen 5 sprites)

*TO RUN*
-------------------------------------------------------------------------------------------------------------------------------------

Add an image into the main './pokesprites' folder, run 'picgen.py'.
On run, you'll be prompted for the name of the image, type this in (with file extension)

i.e.
    'pokesprites.png'

The program will run (slowly), on completion an output image will be added to the main pokesprites folder


*WAYS TO IMPROVE*
-------------------------------------------------------------------------------------------------------------------------------------

Optimise code by:

    - using threading

    - not calculating euclidian distance for all 151 sprites for each & every pixel

    - using a different way of getting avg colour, in order to remove i/o writing & reading temp imgs

    - use sprites with less whitespace (sprites that fill majority 32x32 pixel space)

        - I did search for these, but all sprites I could find had whitespace or were different sizes


*OTHER SCRIPTS*
-------------------------------------------------------------------------------------------------------------------------------------

'pokesprites.py' is used to generate a dictionary of all sprites & their mean rgb colour value, this dictionary is pickled & imported on run into picgen.py

'pokespritesextractor.py' is used to extract individual sprites from gen5icons-sheet, i then manually deleted all but the original 151 sprites.
