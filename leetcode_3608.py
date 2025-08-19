'''
URL := https://leetcode.com/problems/minimum-time-for-k-connected-components/description/
3608. Minimum Time for K Connected Components

Complexity
T = 
S = 

Approaches : Binary Search, Union Find, DFS/BFS
15 minutes passed yet again WOOOH
'''
class Solution:

    # adjList = makeAdjList(edges,targetTime))
    def makeAdjList(self, n,edges,targetTime) -> dict():
        # woah such conciseness ( and key setting too ) 
        adjList = dict()
        for x in range(n):
            adjList[x] = dict()
        for [u,v,t] in edges:
            # else, add vertices -> not edges
            # add edge if time >= targetTime
            if(t > targetTime):
                adjList[u][v] = targetTime
                adjList[v][u] = targetTime
        return adjList

    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:
        # that corner case : already exists SMH
        targetAns = float('inf')
        # Find the minimum t : get # of connected components
        # k guaranteed it's existence :-)
        low = 0
        high = (int)(pow(10,9))
        while(low <= high):
            mid = (int)((low + high) // 2)
            adjList = self.makeAdjList(n,edges,mid)
            numComponents = self.getConnCompCount(adjList,mid)
            if(numComponents < k):
                low = mid + 1
            # have at least k connected components here
            elif(numComponents >= k):
                targetAns = min(targetAns,mid)
                high = mid - 1
        return targetAns

    def getConnCompCount(self,adjList,mid) -> int:
        compCount = 0
        visited = set()
        for vert,children in adjList.items():
            if(vert not in visited):
                self.dfs(vert,adjList,visited)
                compCount += 1
        return compCount

    def dfs(self,vert,adjList,visited) -> None:
        if(vert not in visited):
            visited.add(vert)
            children = adjList[vert]
            for child,childDist in children.items():
                self.dfs(child,adjList,visited)
