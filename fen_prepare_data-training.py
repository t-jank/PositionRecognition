# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:35:55 2024

@author: t-jan
"""

path = "C:\\Users\\t-jan\\Desktop\\PositionRecognition\\training-data\\boards2\\fen.txt"

with open(path, "r") as txt:
    lines = txt.readlines()

"""
list1 = list(lines[0])
for i in range(0,1280):
    if list1[i] == 'x': list1[i] = '0'
    elif list1[i] == 'p': list1[i] = '1'
    elif list1[i] == 'n': list1[i] = '2'
    elif list1[i] == 'b': list1[i] = '3'
    elif list1[i] == 'r': list1[i] = '4'
    elif list1[i] == 'q': list1[i] = '5'
    elif list1[i] == 'k': list1[i] = '6'
    elif list1[i] == 'P': list1[i] = '7'
    elif list1[i] == 'N': list1[i] = '8'
    elif list1[i] == 'B': list1[i] = '9'
    elif list1[i] == 'R': list1[i] = '4'
    elif list1[i] == 'Q': list1[i] = '5'
    elif list1[i] == 'K': list1[i] = '6'
#list1[2] = 'U'
lines[0] = ''.join(list1)
"""

def CutEndings(fen):
    sp = fen.find(" ")
    fen = fen[:sp]+"\n"
    return fen

def EmptySquaresAsXs(fen):
    for j in range(0,len(fen)):
        for i in range(0,len(fen)):
            if fen[i].isnumeric() == True:
                tmpline = fen[:i] + int(fen[i])*'x' + fen[i+1:]
                fen = tmpline
                break
    return fen

def RemoveSlashes(fen):
    fen = fen.replace('/','')
    return fen

def Save():
    with open(path, "w") as txt:
        dupa = "".join(lines)
        txt.write(dupa)

"""
for i in range(0,20,2):
    lines[i] = CutEndings(lines[i])
    lines[i] = EmptySquaresAsXs(lines[i])
    lines[i] = RemoveSlashes(lines[i])
    Save()
"""

#for i in range(0,10):
#    lines[i] = lines[i][:len(lines[i])-1]



