# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:31:44 2019

@author: selva
"""

def move( start, end):
    print("Move from {0} to {1}".format(start, end))

def tower(height,start, end, spare):
    if height == 1:
        move(start, end)
    else:
        tower(height-1,start, spare, end)
        tower(1, start, end, spare)
        tower(height-1, spare, end, start)
        
tower(3,'a','b', 'c')