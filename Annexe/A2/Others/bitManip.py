# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 16:43:58 2020

@author: chevrier6
"""

######################
def mask16(v):
    "same as setBit(v,0)"
    b=1
    for i in range(v):
        b*=2
    return b

# 4 next functions from https://wiki.python.org/moin/BitManipulation
# testBit() returns a nonzero result, 2**offset, if the bit at 'offset' is one.
def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)

  # setBit() returns an integer with the bit at 'offset' set to 1.

def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)

 # clearBit() returns an integer with the bit at 'offset' cleared.

def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)

 # toggleBit() returns an integer with the bit at 'offset' inverted, 0 -> 1 and 1 -> 0.

def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)