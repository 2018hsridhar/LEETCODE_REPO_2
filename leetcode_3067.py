'''
URL := https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/
3067. Count Pairs of Connectable Servers in a Weighted Tree Network
'''
class Solution:

    # Always valid tree : no solo node here
    # we still need edge weighting though -> store in adjList at least
    def buildAdjList(self, edges: List[List[int]]) -> dict:
        adjList = {}
        for edge in edges:
            src = edge[0]
            dst = edge[1]
            weight = edge[2]
            # gaaah map() function no work by itself whyy!!
            if src not in adjList:
                adjList[src] = {}
            if dst not in adjList:
                adjList[dst] = {}
            if dst not in adjList[src]:
                adjList[src][dst] = weight
            if src not in adjList[dst]:
                adjList[dst][src] = weight
        return adjList

    # it's not ordered -> go put an ordering later ( or order the adjList too )
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        adjList = self.buildAdjList(edges)
        count_keys = len(adjList)
        # print(adjList)
        pairCounts = [0 for i in range(count_keys)]
        # print(pairCounts)
        for srcNode in range(count_keys):
            # `NameError` no definitions compilation err
            # `self` be like a package name too
            childCount = self.countCandidates(srcNode,adjList)
            for i in range(len(childCount)):
                for j in range(1,len(childCount),1):
                    leftProd = childCount[i]
                    rightProd = childCount[j]
                    pairCounts[srcNode] += (leftProd * rightProd)
        return pairCounts
        
    # Feeling tired should go to sleep too
    def countCandidates(self, srcNode:int,adjList:dict) -> List[int]:
        # it's within each path that we append the candidate -> list of list type of thing
        countCandidates = []
        frontierChild = adjList[srcNode]
        for dst, weight in frontierChild:
            visited = set()
            countOnThePath = self.dfsCount(dst,adjList,visited,weight)
            countCandidates.append(countOnThePath)
        return countCandidates

    def dfsCount(self, dst:int, )

