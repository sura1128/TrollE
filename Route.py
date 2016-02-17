#Route File
import Queue
class Route:

    def __init__(self, source, destination, dist, visited,P):
        self.__source = source
        self.__destination = destination
        self.__dist = [999,999,999,999,999,999,999,999,999,999,999,999]
        self.__visited = [False,False,False,False,False,False,False,False,False,False,False,False]
        self.__P=[0,0,0,0,0,0,0,0,0,0,0,0]


    def findRoute(self):
        from time import time
        start = time()
##        matrix = [[0,8,6,4,5,7,0,0,0,0,0,0],
##                  [8,0,2,0,0,0,0,0,0,0,3,0],
##                  [6,2,0,2,0,0,0,0,0,3,0,0],
##                  [4,0,2,0,1,0,0,0,2,0,0,0],
##                  [5,0,0,1,0,2,0,4,0,0,0,0],
##                  [7,0,0,0,2,0,3,0,0,0,0,0],
##                  [0,0,0,0,0,3,0,1,0,0,0,0],
##                  [0,0,0,0,4,0,1,0,0,0,0,2],
##                  [0,0,0,2,0,0,0,0,0,0,0,1],
##                  [0,0,3,0,0,0,0,0,0,0,2,2],
##                  [0,3,0,0,0,0,0,0,0,2,0,0],
##                  [0,0,0,0,0,0,0,2,1,2,0,0]]

        adjList = {}
        adjList[0] = [(1,8), (2,6), (3,4), (4,5), (5,7)]
        adjList[1] = [(0,8), (2,2), (10,3)]
        adjList[2] = [(0,6), (1,2), (3,2), (9,3)]
        adjList[3] = [(0,4), (2,2), (4,1), (8,2)]
        adjList[4] = [(0,5), (3,1), (5,2), (7,4)]
        adjList[5] = [(0,7), (4,2), (6,3)]
        adjList[6] = [(5,3), (7,1)]
        adjList[7] = [(4,4), (6,1), (11,2)]
        adjList[8] = [(3,2), (11,1)]
        adjList[9] = [(2,3), (10,2), (11,2)]
        adjList[10] = [(1,3), (9,2)]
        adjList[11] = [(7,2), (8,1), (9,2)]
       
            
        Q = Queue.PriorityQueue()
        Q.put((0,self.__source))
        self.__dist[self.__source] = 0

        while (Q.qsize() != 0):
            u = Q.get()[1]
            
            if (u == self.__destination):
                break;

            for x in range(0,len(adjList[u])):
                if (self.__dist[adjList[u][x][0]] > self.__dist[u] + adjList[u][x][1]):
                        self.__dist[adjList[u][x][0]] = self.__dist[u] + adjList[u][x][1]
                        Q.put((self.__dist[adjList[u][x][0]],adjList[u][x][0]))
                        self.__P[adjList[u][x][0]] = u
            
##            for x in range(0,12):
##                if (matrix[x][u] != 0):
##                    if (self.__dist[x] > self.__dist[u] + matrix[u][x]):
##                        self.__dist[x] = self.__dist[u] + matrix[u][x]
##                        Q.put((self.__dist[x],x))
##                        self.__P[x] = u

        path = []
        x = self.__destination

        while (True):
            path.append(x)
            x = self.__P[x]
            if (x==self.__source):
                path.append(x)
                break;

        path = self.reverseList(path)
        end = time()

        print ("Time = ", end-start)
            
        return (path)

    def reverseList(self, path):
        return list(reversed(path))






