# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 18:03:40 2024

@author: t-jan
"""


def ReverseBoard(FEN):
    splited_fen = FEN.split()
    splited_fen[0] = splited_fen[0][::-1]
    FEN = " ".join(splited_fen)
    return FEN



FEN = "r1b2r1k/ppp4p/3p4/3Pbpq1/B4N2/2P5/PP2Q1PP/R4RK1 w - - 0 1"

print(ReverseBoard(FEN))
