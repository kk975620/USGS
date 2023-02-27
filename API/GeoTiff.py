import os
from os import listdir
from os.path import isfile, join
import math


#look up for the .tiff file based on the x and y coordinates
#and position of x and y (north, south, east or west)
def lookUpForImageFile(x, y, xpos, ypos):
    xceil = math.ceil(abs(x))
    yceil = math.ceil(abs(y))
    if x >= 100:
        lookUpFileStr = ypos + str(yceil) + xpos + str(xceil) +".tif"
    else:
        lookUpFileStr = ypos + str(yceil) + xpos + "0" + str(xceil) +".tif"
    onlyFiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    fileFound = 0
    fileName = ''
    for i in onlyFiles:
        if lookUpFileStr in i:
            fileName = i
            fileFound = 1

    if fileFound:
        return fileName
    else:
        return "notfound"


#function to determine if the x-coordinate lies west or east of greewich meridian
def determine_x_position(x):
    if(x<0):
        return 'w'
    else:
        return 'e'

#function
def determine_y_position(y):
    if(y<0):
        return 's'
    else:
        return 'n'
