'''
2359. Find Closest Node to Given Two Nodes
URL := https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/
'''
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        numNodes = len(edges)
        adjList = dict()
        for index,edge in enumerate(edges):
            adjList[index] = edge
        distancesOne = [float('inf') for idx in range(numNodes)]
        distancesTwo = [float('inf') for idx in range(numNodes)]
        visited = set()
        self.dfs(node1,adjList, distancesOne, 0,visited)
        visited.clear()
        self.dfs(node2,adjList, distancesTwo, 0,visited)
        maxDistance = float('inf')
        bestAnswer = -1
        for index, (distOne,distTwo) in enumerate(zip(distancesOne,distancesTwo)):
            minMaxDist = max(distOne,distTwo)
            if(minMaxDist < maxDistance):
                maxDistance = minMaxDist
                bestAnswer = index
        return bestAnswer

    # handle recursion depth ( if already visited ) 
    def dfs(self, parent:int, adjList:dict, distances:List[int], curDist:int, visited:set):
        visited.add(parent)
        distances[parent] = curDist
        child = adjList[parent]
        childDist = curDist + 1
        if(child != -1 and child not in visited):
            self.dfs(child,adjList,distances,childDist, visited)







        
        
