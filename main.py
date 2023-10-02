# -*- coding: utf-8 -*-
from graph import Graph


def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == g.num_vertices):
                break
            g.matrix[l][c] = int(i)
            if(g.matrix[l][c] > 0):
                g.list[l].append(c)
            
            c += 1
        l += 1
    return g

gr = load_from('./instncias_grafo/pcv4.txt')
gr.print()
# dist, ant = gr.bfs(0)
# print(dist)
# print(ant)
# Graph.path_between_nodes(ant,0,3)
gr.dfs(0)