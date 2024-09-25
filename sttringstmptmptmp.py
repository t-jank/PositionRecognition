# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:35:55 2024

@author: t-jan
"""

path = "C:\\Users\\t-jan\\Desktop\\PositionRecognition\\training-data\\boards\\fen.txt"

with open(path, "r") as txt:
    lines = txt.readlines()

print(lines[0][0])

'''
for i in range(0,40,2):
    sp = lines[i].find(" ")
    lines[i] = lines[i][:sp]+"\n"
'''
'''
for lll in range(0,39,2):
    for j in range(0,len(lines[lll])):
        for i in range(0,len(lines[lll])):
            if lines[lll][i].isnumeric()==True:
                tmpline=lines[lll][:i]+ int(lines[lll][i])*'x' + lines[lll][i+1:]
                lines[lll]=tmpline
                break
'''
'''
for du in range(0,39,2):
    lines[du] = lines[du].replace('/','')
'''
'''
for i in range(0,20):
    lines[i] = lines[i][:len(lines[i])-1]
'''
'''
with open(path, "w") as txt:
    dupa = "".join(lines)
    txt.write(dupa)
'''

