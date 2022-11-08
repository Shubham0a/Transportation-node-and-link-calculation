#------------------------------------------------------------------------------------
#       *******************************
#*****************Shubham kumar***********
#       *******************************

#  This program is intended to find shortest distance between two node of street
#  This program was developed in *2022, so if you are using this code there can be some changes later
#     *************** lets start ****************

# pre-requisite:
#       some packages that needs to be installed
#                   **pip install osm2gmns
#
#  Download map.osm file from https://www.openstreetmap.org
#------------------------------------------------------------------------------------\

# this code converts map.osm file into two file link.csv and node .csv
import os
import osm2gmns as og
CURRENT_DIR = os.getcwd()
filename = os.path.join(CURRENT_DIR,'map.osm')
network = og.getNetFromFile(filename, default_speed=True, default_lanes=True)
og.outputNetToCSV(network)
print(filename)

# this shows the position of node
import csv
with open('node.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t node-id {row[1]} x-coordinate {row[9]} , y-coordinate {row[10]}.')
            line_count += 1
    node = line_count-1
    print(f'Number of Node = {node}')
    

# this shows the length from one node to other
with open('link.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            print(f'\t from node-id {row[3]} to node-id {row[4]} length {row[6]}.')
            line_count += 1
    print(f'No. of link = {line_count-1}.')

# storing the values of distances from one node to other
import numpy as np
arrr = np.zeros((node,node),dtype='float')

with open('link.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            a=int(row[3])
            b=int(row[4])
            d=float(row[6])
            arrr[a][b] = d
            line_count += 1
    print(f'No. of link = {line_count-1} and node = {node} processed.')


zeroes_array = []
for i in range(0,node):
  array = [0]*node
  for j in range(0,node):
    array[j]= arrr[i][j]
  # print(array)
  zeroes_array.append(array)

# dijkstra algorithms for for finding minimum possible length
import sys
class Graph():
 # Size of the array will be the no. of the vertices "V" here V will be 20+1
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

 #Function to print the answers
    def printSolution(self, dist):
        print("Node \tDistance from Node 0(in M)")
        for node in range(self.V):
            print(node, "\t", dist[node])
 
    #An untility funcion to find the min distanced vertex which isn't included in the shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search for not the nearest vertex i.e not in the shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    # Function to implements Dijkstra's single source shortest path algorithm
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # x is always equal to src in first iteration
            x = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the shortest path tree
            sptSet[x] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and \
                        dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
 
        self.printSolution(dist)
 
# Driver's code
if __name__ == "__main__":
    g = Graph(node)
    #It contains a total nodes from chosen from .csv file
    #The speed limit on all the links b/w these two nodes is 100 kmph and hence
    #temporal distance is equal to spatial distance
    #all the distances in the following graph is in meters
    g.graph = zeroes_array

    g.dijkstra(0)

#------------------------------------------------------------------------------------
#       *******************************
#*****************Shubham kumar***********
#       *******************************
#------------------------------------------------------------------------------------
