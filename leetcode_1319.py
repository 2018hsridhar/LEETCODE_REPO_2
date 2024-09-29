Intuition and Approach
See problem title

Complexity
V:=#−vertices
E:=#−edges

Time complexity:
O(V+E)

Space complexity:
O(VE) ( explicit )
O(1) ( implicit )

Code
'''
1319. Number of Operations to Make Network Connected
URL := https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
'''
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        minNumConn = -1
        visited = set()
        totalNumExtraEdges = 0
        numberConnComps = 0 
        adjList = self.makeAdjList(n,connections)
        numberUniqEdges = 0
        numEdges = len(connections)
        for x in range(n):
            if(x not in visited):
                numberEdgesInComp = self.bfs(visited, x, adjList)
                numberUniqEdges += numberEdgesInComp
                numberConnComps += 1
        totalNumExtraEdges = numEdges - numberUniqEdges
        numEdgesNeeded = numberConnComps - 1
        if(totalNumExtraEdges >= numEdgesNeeded):
            minNumConn = numEdgesNeeded
        return minNumConn

    # get correct edge counting here
    # I have ac ount of number of unique edges at least
    def bfs(self, visited: set(), startNode: int, adjList: dict()) -> int:
        numExtraConns = 0
        queue = []
        queue.append(startNode)
        numUniqueEdges = 0
        visitedChild = set()
        while(len(queue) > 0):
            parent = queue.pop(0)
            visitedChild.add(parent)
            if(parent not in visited):
                visited.add(parent)
                children = adjList[parent]
                for child in children:
                    if(child not in visited):
                        queue.append(child)
                    if(child not in visitedChild):
                        numUniqueEdges += 1
                        visitedChild.add(child)
        return numUniqueEdges

    def makeAdjList(self, n:int, connections: List[List[int]]) -> dict():
        adjList = dict()
        for node in range(n):
            adjList[node] = set()
        # like javascript -> array destructuring
        for [src,dst] in connections:
            adjList[src].add(dst)
            adjList[dst].add(src)
        return adjList
