# 2204. Distance to a Cycle in Undirected Graph
# URL := https://leetcode.com/problems/distance-to-a-cycle-in-undirected-graph/description/\

# Intutions : 
# Precache computation : large number of nodes involved
# One cycle @ max invariant

# Approach :

# Complexity
# Let V := #-vertices
# Let E := edges ( equal to V in this case )
# Time := O(V+E) = O(V)
# Space := O(V) ( E ) O(1) ( IMP ) 
# 15 minutes meat of problem ( cycle detection undirected graphs )

from collections import deque

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        minDistances = [float('inf') for i in range(n)]
        startNode = 0
        adjList = self.makeAdjList(n,edges)
        nodesVisited = set()
        edgesVisited = dict()
        cycleNodes = set()
        cycleStatus = self.detectCycle(startNode, adjList, nodesVisited, edgesVisited, cycleNodes)
        startDist = 0
        visited = set()
        for startNode in cycleNodes:
            self.computeMinDist(startNode, adjList, visited, cycleNodes, minDistances, startDist)
        return minDistances

# it's undirected : not directed gaaaahhhh
# you solved a directed case of it -> solve undirected
# level order traversal from the nodes in the cycle as the "root" nodes in the system
# undirected is a BFS expansion from the cycle nodes :-)
    def computeMinDist(self, parentNode: int, adjList: dict(),
        visited: set(), cycleNodes: set(), minDistances: List[int], curDist: int):
        if(parentNode not in visited):
            visited.add(parentNode)
            minDistToCycle = curDist
            if(parentNode in cycleNodes):
                minDistances[parentNode] = 0
                curDist = 0
            else:
                minDistances[parentNode] = curDist
            children = adjList[parentNode]
            for child in children:
                self.computeMinDist(child,adjList,visited,cycleNodes,minDistances,curDist + 1)

    def makeAdjList(self, n:int, edges: List[List[int]]) -> dict():
        adjList = dict()
        for i in range(n):
            adjList[i] = set()
        for edge in edges:
            src = edge[0]
            dst = edge[1]
            adjList[src].add(dst)
            adjList[dst].add(src)
        return adjList

    def detectCycle(self, parentNode, adjList: dict(), 
                    nodesVisited: set(), edgesVisited: dict(), cycleNodes: set()) -> List[int]:
        cycleStatus = -1
        if(parentNode not in nodesVisited):
            nodesVisited.add(parentNode)
            children = adjList[parentNode]
            for child in children:
                if(child not in nodesVisited):
                    
                    # bidir graph : please add both edges
                    if(parentNode not in edgesVisited):
                        edgesVisited[parentNode] = set()
                    if(child not in edgesVisited):
                        edgesVisited[child] = set()
                    edgesVisited[parentNode].add(child)
                    edgesVisited[child].add(parentNode)

                    childStatus = self.detectCycle(child,adjList,nodesVisited,edgesVisited,cycleNodes)
                    if(childStatus[1] != -1):
                        # the node of the cycle hit ( see as a start node )
                        if(childStatus[1] == parentNode):
                            cycleNodes.add(parentNode)
                            return [-1,-1]
                        else:
                            cycleNodes.add(parentNode)
                            return [parentNode,childStatus[1]]
                elif(child in nodesVisited):
                    # no cycle detected : was an already traversed edge
                    if(not(parentNode in edgesVisited and child in edgesVisited[parentNode])):
                        cycleNodes.add(child)
                        cycleNodes.add(parentNode)
                        return [child,child]
                    # we have a cycle detected here!
        return [-1,-1]

