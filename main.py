import os
import sys
from scipy import misc
from imageio import imread
from imageio import imwrite


def isBlack(pixel):
    return pixel[0] == 0 and pixel[1] == 0 and pixel[2] == 0


def task(inputFile1, inputFile2, outpurFile):
    try:
        leftImage  = imread(inputFile1)
        rightImage = imread(inputFile2)

    except FileNotFoundError:
        print('Error: input files not found!')
        return

    leftDimensions  = [len(leftImage), len(leftImage[0])]
    rightDimensions = [len(rightImage), len(rightImage[0])]

    if leftDimensions != rightDimensions:
        print('Error: images have different dimensions!')
        return

    height = leftDimensions[0]
    width  = leftDimensions[1]

    for i in range(0, height):
        for j in range(0, width):
            if isBlack(rightImage[i][j]):
                brightness = 0
                for k in range(3):
                    brightness += leftImage[i][j][k]

                brightness = brightness // 3
                for k in range(3):
                    leftImage[i][j][k] = brightness

    try:
        imwrite(outpurFile, leftImage, format='bmp')
    except FileNotFoundError:
        print('Error: output failure!')

    return


inputFile1 = sys.argv[1]
inputFile2 = sys.argv[2]
outputFile = sys.argv[3]

try:
    task(inputFile1, inputFile2, outputFile)
except FileNotFoundError:
    print('Failure! Program terminated!')