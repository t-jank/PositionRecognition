# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 20:55:06 2024

@author: t-jan
"""

from PIL import Image, ImageDraw
import math

def ChangeContrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def Contrast(c):
        return 128 + factor * (c - 128)
   # im.point(contrast).show()
    return img.point(Contrast)

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

def Crop(image):
    left = 0
    top = 7*int(image.height / 8)
    right = int(image.width / 8)
    bottom = 8*int(image.height / 8)
    # Cropped image of above dimension
    # (It will not change original image)
    im1 = image.crop((left, top, right, bottom))
    return im1

def SquareCoordinates(square):
    def SquareNumber(square_name):
        def LetterNumber(letter):
            return ord(letter.lower())-96
        return LetterNumber(square_name[0]) + (int(square_name[1])-1)*8
    def SquareCoordinates(square_number):
        column = square_number % 8
        if column == 0: column = 8
        row = math.ceil(square_number/8)
        return column, row
    square_number = SquareNumber(square)
    square_coordinates = SquareCoordinates(square_number)

    return square_coordinates

def ExtractSquare(image, square):
    col, row = SquareCoordinates(square)
    square_width = int(image.width/8)
    square_height = int(image.height/8)
    left = (col-1) * square_width
    right = left + square_width
    top = (8-row) * square_height
    bottom = top + square_height
    square_image = image.crop((left, top, right, bottom))
    return square_image


image = Image.open('C:\\Users\\t-jan\\Desktop\\PositionRecognition\\Screenshot_19.jpg').convert('L')
#image.show()
a = ChangeContrast(image, 100)
#a.show()
b = DrawGrid(a)
b.show()

d = ExtractSquare(b, 'c2')
d.show()

"""
def change_contrast_multi(img, steps):
    width, height = img.size
    canvas = Image.new('RGB', (width * len(steps), height))
    for n, level in enumerate(steps):
        img_filtered = ChangeContrast(img, level)
        canvas.paste(img_filtered, (width * n, 0))
    return canvas

change_contrast_multi(im, [50, 75, 100])
"""

