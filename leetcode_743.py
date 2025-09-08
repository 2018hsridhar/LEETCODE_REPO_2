'''
URL := https://leetcode.com/problems/network-delay-time/description/
743. Network Delay Time

Get shortest path : source node -> to all other nodes
Directed edges
No parallel edges
Any cycles ( maybe ) ( but no self-loops )
Fits into RAM
'''

import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = dict()
        for vert in range(1,n+1,1):
            adjList[vert] = dict()
        for [u,v,w] in times:
            adjList[u][v] = w
        INF = float('inf')
        # Del first element ( ShortestPathAlgo ) 
        shortestDists = [INF for vert in range(0,n+1,1)]
        visited = set()
        frontier = []
        # ROOT INITIALIZATION
        shortestDists[k] = 0
        heapq.heappush(frontier,[0,k])
        # Djkstra's : loop, visited, greedy, shortest distance weight added to heap
        # Djkstra's is correct -> rederive : strictly heap based operations
        # but gaah memory limit exceeded WTF???
        while(len(frontier) > 0):
            [parentDist,parent] = heapq.heappop(frontier)
            visited.add(parent)
            children = adjList[parent]
            for child,childWeight in children.items():
                if(child not in visited):
                    curChildDist = shortestDists[child]
                    candidChildDist = shortestDists[parent] + childWeight
                    if(candidChildDist < curChildDist):
                        shortestDists[child] = candidChildDist
                        childRecord = [shortestDists[child],child]
                        heapq.heappush(frontier,childRecord)
        shortestDists.pop(0)
        maxDist = max(shortestDists)
        if(maxDist == INF):
            return -1
        return maxDist
        
