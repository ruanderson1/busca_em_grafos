# -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]
        

    def print(self):
        print(self.matrix)
        print(self.list)


        
    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        isVisited[source] = True
        dist[source] = 0
        
        while Q.empty() != True:
            p = Q.get()
            print("Vertice: " + str(p))
            
            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True
        
        return dist, ant
    

    # -*- coding: utf-8 -*-
import queue

class Graph:
    def __init__(self, n):
        self.num_vertices = n
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.list = [[] for _ in range(n)]
        

    def print(self):
        print(self.matrix)
        print(self.list)


        
    def bfs(self, source):
        dist = [-1 for _ in range(self.num_vertices)]
        ant = [-1 for _ in range(self.num_vertices)]
        isVisited = [False for _ in range(self.num_vertices)]
        Q = queue.Queue()
        Q.put(source)
        isVisited[source] = True
        dist[source] = 0
        
        while Q.empty() != True:
            p = Q.get()
            print("Vertice: " + str(p))
            
            for v in self.list[p]:
                if isVisited[v] == False:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.put(v)
                    isVisited[v] = True
        
        return dist, ant
    

    #-----------------------------------
    # FUNÇÃO PEDIDA NA ATIVIDADE 1     -
    #-----------------------------------

    def path_between_nodes(ant, source, dest):
        destination=dest
        if ant[destination] == -1:
            print("Não há caminho entre os nós")
            return

        path = []
        while destination != -1:
            path.insert(0, destination)
            destination = ant[destination]
            
        print("Caminho entre os nós {} e {}: {}".format(source, dest, "->".join(map(str, path))))


    #-----------------------------------
    # FUNÇÃO PEDIDA NA ATIVIDADE 2     -
    #-----------------------------------

    def dfs(self,source):
        visited = [ False for _ in range( self.num_vertices )]
        stack = []
        stack.append(source)

        while(stack):
            p = stack.pop()

            if not visited[p]:
               print( "vertice: " + str(p))
               visited[p] = True

               for neighbor in self.list[p]:
                   if not visited[neighbor]:
                      stack.append(neighbor)