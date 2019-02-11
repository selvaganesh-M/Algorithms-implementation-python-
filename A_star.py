# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:42:41 2019

@author: selva
"""

import math

def nodes_input():
    nodes = input("Enter parent and connected nodes : ")
    if(nodes=='$'):
        return ['$',0]
    nodes = [x for x in nodes.split()]
    weights = weight_inputs(len(nodes)-1)
    return [nodes, weights]
    
    
def weight_inputs(n):
    weights = input("Enter weights : ").split()
    if(len(weights)!=n):
        print("number of weights doesnt match")
        weights = weight_inputs(n)
    return weights
    

def graph_input():
    graph = {}
    print("Enter $$ to submit")
    while True:
        
        nodes, weights = nodes_input()
        if(nodes[0] == '$'):
            break
        else:
            parent = nodes[0]
            nodes = nodes[1:]
            pair = [(nodes[i],weights[i]) for i in range(len(weights))]
            graph[parent] = pair
        
    return graph
        

graph ={  's': [('a', '7'), ('b', '2'), ('c', '3')],\
          'a': [('s', '7'), ('b', '3'), ('d', '4')],\
          'b': [('s', '2'), ('a', '3'), ('h', '4')],\
          'c': [('s', '3'), ('l', '2')],\
          'd': [('a', '4'), ('b', '4'), ('h', '1'), ('f', '6')],\
          'f': [('d', '6'), ('h', '3')],\
          'g': [('h', '2'), ('e', '2')],\
          'h': [('f', '3'), ('d', '1'), ('b', '1'), ('g', '2')],\
          'e': [('g', '2'), ('k', '5')],\
          'l': [('c', '2'), ('i', '4'), ('j', '4')],\
          'i': [('l', '4'), ('j', '6'), ('k', '4')],\
          'j': [('l', '4'), ('i', '6'), ('k', '4')],\
          'k': [('i', '4'), ('j', '4'), ('e', '5')]}

class graph_analysis:
    
    
    def __init__(self, graph):
      
        self.graph = graph 
        
        self.paths_analysed_from = []

        self.analysed_start_nodes = []        
        
    def analyse(self, start):
        
        self.analysed_start_nodes.append(start)
        
        expanded = [start]
        
        queue = [(start,0)]
        
        all_nodes = [node for node in self.graph]
        
        node_weights = [math.inf for i in range(len(all_nodes))]
        
        node_weights[all_nodes.index(start)] = 0
        
        parent = ['#' for i in range(len(all_nodes))]
        
        parent[all_nodes.index(start)] = '-'

    
        try:
            while(len(expanded)!=len(self.graph)):
                
                if(len(queue)==0):
                    break
                
                to_be_expanded = queue[0][0]
                queue = queue[1:]
                parent_index = all_nodes.index(to_be_expanded)
                connected = [x for x in self.graph[to_be_expanded] if x[0] not in expanded]
                
                
                for i in connected:
                    
                    current_node = i[0]
                    
                    current_node_index = all_nodes.index(current_node)
                    
                    parent_weight_from_src = node_weights[parent_index]
                    
                    current_weight = parent_weight_from_src+float(i[1])
                    
                    prev_weight = node_weights[current_node_index]
                    
        
                    if(current_weight<prev_weight):
                        
                        node_weights[current_node_index] = current_weight
        
                        parent[current_node_index] = to_be_expanded
        
                        
                    queue.append((current_node,node_weights[current_node_index]))
        
                    expanded.append(current_node)
                    
                queue.sort(key = lambda k:k[1])
                
        except IndexError:
            print("Graph analysis completed")
        
        details = {"Node":["parent", "distance"]}
        details_list = []
        
        for i in range(len(all_nodes)):
            
            details[all_nodes[i]] = [parent[i], node_weights[i]]
            details_list.append([all_nodes[i],parent[i], node_weights[i]])
            

            
        self.paths_analysed_from.append([start,details_list])
        return self.paths_analysed_from[-1]
        
    

object = graph_analysis(graph)

s = object.analyse("s")

a = object.analyse("a")

b = object.analyse("b")

c = object.analyse("c")

d = object.analyse("d")

e = object.analyse("e")

f = object.analyse("f")

g = object.analyse("g")

h = object.analyse("h")

i = object.analyse("i")

j = object.analyse("j")

k = object.analyse("k")

l = object.analyse("l")










