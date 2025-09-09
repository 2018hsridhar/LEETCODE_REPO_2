'''
3604. Minimum Time to Reach Destination in Directed Graph
URL := https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/description/

SPA - ShortestPathAlgorithm with Djkstra's Algo
'''

import heapq

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        adjList = dict()
        for node in range(n):
            adjList[node] = dict()
        for [u,v,s,e] in edges:
            # multiple edges case ( ahhhh I see ) 
            # it's not a single edge
            # correct approach -> but we want a min time ( iterate over each edge type of thing )
            if(v not in adjList[u]):
                adjList[u][v] = list()
            adjList[u][v].append([s,e])
        for k, v in adjList.items():
            for l,m in v.items():
                m.sort(key = lambda x : (x[0],x[1]))
        # print(adjList)
        ROOT = 0
        INF = float('inf')
        shortestDists = [INF for node in range(n)]
        frontier = []
        ROOT = 0
        parentRec = [0,ROOT]
        # initialize shortestDists global state capture
        shortestDists[ROOT] = 0 
        heapq.heappush(frontier,parentRec)
        visited = set()
        while(len(frontier) > 0):
            [parentDist,parentNode] = heapq.heappop(frontier)
            children = adjList[parentNode]
            visited.add(parentNode)
            for child,childRanges in children.items():
                for childRange in childRanges:
                    [start,end] = childRange
                    if(child not in visited):
                        # update distances here
                        curTime = shortestDists[parentNode]
                        childTime = 0
                        if(curTime >= start and curTime <= end):
                            childTime = curTime + 1
                        elif(curTime < start):
                            childTime = start + 1
                        if(childTime > 0 and childTime < shortestDists[child]):
                            shortestDists[child] = childTime
                            childRec = [childTime,child]
                            heapq.heappush(frontier,childRec)
        minTime = shortestDists[n-1]
        if(minTime == INF):
            minTime = -1
        return minTime
