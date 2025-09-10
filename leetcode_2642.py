'''
2642. Design Graph With Shortest Path Calculator
URL := https://leetcode.com/problems/design-graph-with-shortest-path-calculator/description/

HLA ( High-Level Approach ) :
- Leverage Djkstra's SPA
- YAY [] bracket notation !

Complexity
V := #-vertices
E := #-edges
C := #-calls
Time = O(C*(V+E))
Space = O(V+E) ( Exp ) O(1) ( Impl ) 
'''

import heapq

class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adjList = dict()
        self.n = n
        for vert in range(n):
            self.adjList[vert] = dict()
        for [src,dst,cost] in edges:
            self.adjList[src][dst] = cost
        
    def addEdge(self, edge: List[int]) -> None:
        [src,dst,cost] = edge
        self.adjList[src][dst] = cost

    def shortestPath(self, node1: int, node2: int) -> int:
        INF = float("inf")
        shortestDists = [INF for vert in range(self.n)]
        shortestDists[node1] = 0
        ROOT = node1
        frontier = []
        parentRec = [0,ROOT]
        heapq.heappush(frontier,parentRec)
        visited = set()
        while(len(frontier) > 0):
            [parentDist,parentNode] = heapq.heappop(frontier)
            children = self.adjList[parentNode]
            for child,childWeight in children.items():
                childDist = parentDist + childWeight
                if(childDist < shortestDists[child]):
                    shortestDists[child] = childDist
                    childRec = [childDist,child]
                    heapq.heappush(frontier,childRec)
        minPathCost = shortestDists[node2]
        if(minPathCost == INF):
            minPathCost = -1
        return minPathCost
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
