# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:55:06 2024

@author: t-jan
"""

from PIL import Image, ImageDraw
import math
import cv2 as cv
import numpy as np


def ChangeContrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def Contrast(c):
        return 128 + factor * (c - 128)
    return img.point(Contrast)


def ExtractBoard(img):
    img = np.array(img)
    def DetectLines(img):
        dst = cv.Canny(img, 50, 200, None, 3)
        # Copy edges to the images that will display the results in BGR
       # cdstP = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
        linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
        return linesP
    lines_detected = DetectLines(img)
    x,y=[],[]
    for i in range(0,len(lines_detected)):
        x.append(lines_detected[i][0][0])
        x.append(lines_detected[i][0][2])
        y.append(lines_detected[i][0][1])
        y.append(lines_detected[i][0][3])
    x.sort(), y.sort()
    omited = 0
    left, right, top, bottom = x[omited], x[0-omited-1], y[omited], y[0-omited-1]
    return image.crop((left, top, right, bottom))


def DrawGrid(image):
    draw = ImageDraw.Draw(image)
    y_start = 0
    y_end = image.height
    step_size = int(image.width / 8)
    for x in range(0, image.width, step_size):
        line = ((x, y_start), (x, y_end))
        draw.line(line, fill=1)
    x_start = 0
    x_end = image.width
    for y in range(0, image.height, step_size):
        line = ((x_start, y), (x_end, y))
        draw.line(line, fill=1)
    del draw
    return image


def ExtractSquare(img_board, square):
    def SquareCoordinates(square):
        def SquareNumber(square_name):
            def LetterNumber(letter):
                return ord(letter.lower())-96
            return LetterNumber(square_name[0]) + (8-int(square_name[1]))*8
        def SquareCoordinates(square_number):
            column = square_number % 8
            if column == 0: column = 8
            row = 9-math.ceil(square_number/8)
            return column, row
        if isinstance(square, str): square_number = SquareNumber(square)
        elif isinstance(square, int): square_number = square
        else: print("Unknown type of square")
        square_coordinates = SquareCoordinates(square_number)
        return square_coordinates
    col, row = SquareCoordinates(square)
    square_width = int(img_board.width/8)
    square_height = int(img_board.height/8)
    left = (col-1) * square_width
    right = left + square_width
    top = (8-row) * square_height
    bottom = top + square_height
    square_image = img_board.crop((left, top, right, bottom))
    return square_image

def SaveExtractedSquares():
    for b in range(1,11):
        pth = "C:\\Users\\t-jan\\Desktop\\PositionRecognition\\training-data\\boards2\\Screenshot_"+str(b)+".jpg"
        image = Image.open(pth).convert('L')
        board = ExtractBoard(image)
    #board.show()
        for s in range(1,65):
            square = ExtractSquare(board, s)
            # przed użyciem sprawdzić numerację
            path = "C:\\Users\\t-jan\\Desktop\\PositionRecognition\\training-data\\squares\\" + str(1280+s+64*(b-1)) + ".jpg" # przed użyciem sprawdzić numerację
            # square.save(path) # przed użyciem sprawdzić numerację

# square = ChangeContrast(square, 100)
#square.show(title = "Square")
