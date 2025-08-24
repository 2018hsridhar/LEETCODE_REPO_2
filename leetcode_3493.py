'''
URL := https://leetcode.com/problems/properties-graph/description/
3493. Properties Graph

SEems to be a set intersection problem TBH
DFS and count number of ConnComps at the end to
'''
class Solution:

    def makeAdjList(self, properties: List[List[int]], k: int) -> dict():
        adjList = dict()
        numVertices = len(properties)
        for idx in range(numVertices):
            adjList[idx] = set()
        for i in range(numVertices):
            propOne = properties[i] 
            setOne = set(propOne)
            for j in range(i+1,numVertices,1):
                propTwo = properties[j]
                setTwo = set(propTwo)
                sizeIntersect = setOne.intersection(setTwo)
                cardinality = len(sizeIntersect)
                if(cardinality >= k):
                    adjList[i].add(j)
                    adjList[j].add(i)
        return adjList

    def execInPlaceDFS(self,adjList,numVertices) -> int:
        numberConnComps = 0
        visited = set()
        for rootNode in range(numVertices):
            if(rootNode not in visited):
                numberConnComps += 1
                frontier = [rootNode]
                while(len(frontier) > 0):
                    parent = frontier.pop(0)
                    if(parent not in visited):
                        visited.add(parent)
                        children = adjList[parent]
                        for child in children:
                            frontier.append(child)
        return numberConnComps
        
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        adjList = self.makeAdjList(properties,k)
        numVertices = len(properties)
        numberConnComps = self.execInPlaceDFS(adjList,numVertices)
        return numberConnComps
