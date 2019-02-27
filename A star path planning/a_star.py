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


def from_file():
    file = open(input("Enter the full file location : "), 'r')
    data = [x for x in file.read().split('\n\n')]
    file.close()
    graph = {}
    for i in data:
        temp = [x for x in i.split('\n')]
        parent = temp[0]
        x,y = [float(y) for y in temp[1].split()]
        pair = []
        connected = [x for x in temp[2].split()]
        weights = [float(x) for x in temp[-1].split()]
        pair = [(connected[k],weights[k]) for k in range(len(connected))]
        graph[parent] = [(x,y)] + pair
    return graph



read_from_file = input("Read graph from file [Y/n] : ")

if ( (read_from_file == 'y' ) | ( read_from_file == 'Y' ) ):
    graph = from_file()
             
else:
    graph = graph_input()
    
    
    
###sample graph
#
#graph = { 'a': [(-5.0, 4.5), ('b', 5.0), ('c', 3.0), ('e', 4.0)],\
#          'b': [(0.5, 4.0), ('a', 5.0), ('d', 2.0), ('h', 5.0)],\
#          'c': [(-2.5, 2.0), ('a', 3.0), ('e', 4.0), ('d', 3.0)],\
#          'd': [(1.0, 2.0), ('c', 3.0), ('g', 2.5), ('j', 7.0)],\
#          'e': [(-6.0, 0.0), ('a', 4.0), ('c', 4.0), ('o', 35.0), ('n', 4.5)],\
#          'f': [(-3.0, 0.0), ('o', 3.0)],\
#          'g': [(0.0, 0.0), ('p', 3.0), ('d', 2.5)],\
#          'h': [(4.0, 4.0), ('b', 5.0), ('i', 4.0)],\
#          'i': [(6.0, 2.0), ('h', 4.0), ('j', 3.5), ('k', 3.5)],\
#          'j': [(5.5, -1.0), ('i', 3.5), ('k', 2.0), ('l', 2.0)],\
#          'k': [(7.0, -1.0), ('i', 3.5), ('l', 3.0)],\
#          'l': [(5.0, -3.0), ('p', 5.5), ('j', 2.0), ('k', 3.0), ('m', 1.5)],\
#          'm': [(4.5, -4.0), ('l', 1.5)],\
#          'n': [(-5.5, -4.0), ('q', 2.0), ('e', 4.5), ('m', 10.0)],\
#          'o': [(-4.0, -1.5), ('e', 3.5), ('f', 3.0), ('p', 4.0)],\
#          'p': [(0.0, -3.0), ('o', 4.0)],\
#          'q': [(-7.0, -5.0), ('n', 2.0)]}    
#    
    
    
class a_star:
    
    def __init__(self, graph):
        self.graph = graph
        
    def eucledian(self, a,b):
        x1,y1 = self.graph[a][0]
        x2,y2 = self.graph[b][0]
        return ((x1-x2)**2+(y1-y2)**2)**0.5
    
    def analyse(self, start, end):
        
        
        expanded = [start]
        
        queue = [(start,0)]
        
        all_nodes = [node for node in self.graph]
        
        node_weights = [math.inf for i in range(len(all_nodes))]
        
        node_weights[all_nodes.index(start)] = 0
        
        parent = ['#' for i in range(len(all_nodes))]
        
        parent[all_nodes.index(start)] = '-'
        
        eucledian_distance = [self.eucledian(all_nodes[i], end) for i in range(len(all_nodes))]

        
        try:
            
            while (end not in expanded):
                to_be_expanded = queue[0][0]
                queue = queue[1:]
                parent_index = all_nodes.index(to_be_expanded)
                connected = [x for x in self.graph[to_be_expanded] if x[0] not in expanded]
                coordinates = connected[0]
                connected = connected[1:]            
                
                for i in connected:
                    
                    current_node = i[0]
                    current_node_index = all_nodes.index(current_node)
                    parent_distance_from_source = node_weights[parent_index]
                    current_weight = parent_distance_from_source + i[1]
                    prev_weight = node_weights[current_node_index]
                        
                    if(current_weight<prev_weight):
                            
                        node_weights[current_node_index] = current_weight
            
                        parent[current_node_index] = to_be_expanded
                    
                    metric_distance = current_weight + self.eucledian(current_node, end)
                    
                    queue.append((current_node,metric_distance))
                    
                    expanded.append(current_node)
                    
                queue.sort(key = lambda l:l[1])
        except IndexError:
            print("Graph analysis complete")
        
        details = {"Node":["parent", "distance"]}

        
        for i in range(len(all_nodes)):
            
            if(node_weights[i] != math.inf):
                details[all_nodes[i]] = [parent[i], node_weights[i]]

        
        trace = [end]
        while trace[-1] != start:
            current = trace[-1]
            trace.append(details[current][0])
        
        return details[end][1], '-'.join(trace[-1::-1]), details
  
    
obj = a_star(graph)

dist, trace, details = obj.analyse('q','b')
