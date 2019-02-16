# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 21:10:20 2019

@author: selva
"""

import math

def nodes_input():
    nodes = input("Enter parent and connected nodes : ")
    if(nodes=='$'):
        return ['$',0, None, None]
    nodes = [x for x in nodes.split()]
    x,y = cod()
    weights = weight_inputs(len(nodes)-1)
    
    return [nodes, weights, x, y]
    
def cod():
    t = [float(x) for x in input("Enter coordinates : ").split()]
    if len(t)!=2:
        print("Enter coordinates properly : ")
        t = cod()
    return t


def weight_inputs(n):
    weights = input("Enter weights : ").split()
    if(len(weights)!=n):
        print("number of weights doesnt match")
        weights = weight_inputs(n)
    return [float(i) for i in weights]
    

def graph_input():
    graph = {}
    print("Enter $ to submit")
    while True:
        
        nodes, weights, x, y = nodes_input()
        if(nodes[0] == '$'):
            break
        else:
            parent = nodes[0]
            nodes = nodes[1:]
            pair = [(nodes[i],weights[i]) for i in range(len(weights))]
            graph[ parent ] = [ ( x , y ) ] + pair
            
    return graph

read_from_file = input("Read graph from file [Y/n] : ").lower()

if read_from_file=='y':
    file = open(input("Enter the full file location : "), 'r')
    data = [x for x in file.read().split('\n\n')]
    file.close()
    graph = {}
    for i in data:
        temp = [x for x in i.split('\n')]
        parent = temp[0]
        x,y = [float(y) for y in temp[1].split()]
        
        
    
else:
    graph = graph_input()