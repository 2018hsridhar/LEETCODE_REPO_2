# 2392. Build a Matrix With Conditions
# URL := https://leetcode.com/problems/build-a-matrix-with-conditions/description/
# Goal : build DAGs are verify that we can build a dag and visit all nodes in our DAG
# Satisfy invariants : problem reduction ( graph problem in the hiding ) 
# Rows and columns treatable as "independent" subproblems :-)
# not everyone follows conditions, but initiate those nodes
# Topological sort and DAGs engered a total ordering of nodes in a graph
# 30 minutes -> close, but almost there at least :-)
class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        rowDagAndGraph = self.buildDag(k,rowConditions)
        colDagAndGraph = self.buildDag(k,colConditions)
        # 0 index the row 
        rowVals = [-1 for i in range(k)]
        colVals = [-1 for i in range(k)]
        rowDagStatus = self.verifyAndAssignDag(k, rowDagAndGraph, rowVals)
        colDagStatus = self.verifyAndAssignDag(k,colDagAndGraph, colVals)
        finalMatrix = []
        if(rowDagStatus and colDagStatus):
            finalMatrix = self.makeFinalMatrix(k,rowVals,colVals)
        return finalMatrix

    # build : colwise, rowwise
    # either rowDag or colDag assignation works : whichever one :-)
    def buildDag(self, k:int, rowConditions: List[List[int]]) -> List[dict()]:
        inDegree = dict()
        adjList = dict()
        for i in range(k):
            inDegree[i] = 0
            adjList[i] = set()
        # handle duplicate edges please
        for edge in rowConditions:
            src = edge[0] - 1
            dst = edge[1] - 1
            if(dst not in adjList[src]):
                adjList[src].add(dst)
                inDegree[dst] += 1
        return [inDegree, adjList]

    # each val a row ( 0 ) or col ( 0) -> 
    def verifyAndAssignDag(self, k: int, dagAndGraph: List[dict()], assignedVals: List[int]) -> None:
        dag = dagAndGraph[0]
        graph= dagAndGraph[1]
        queue = []
        seqNum = 0
        numVisitedNodes = 0
        # never have to delete info from our DAG too :-)
        for node,inDeg in dag.items():
            if(inDeg == 0):
                queue.append(node)
        while(len(queue) > 0):
            parentNode = queue.pop(0)
            numVisitedNodes += 1
            assignedVals[parentNode] = seqNum
            seqNum += 1
            children = graph[parentNode]
            for child in children:
                dag[child] -= 1
                if(dag[child] == 0):
                    queue.append(child)
        return (numVisitedNodes == k)

    def makeFinalMatrix(self, k:int, rowVals:List[int], colVals:List[int]) -> List[List[int]]:
        finalMatrix = [[0 for j in range(k)] for i in range(k)]
        for idx in range(k):
            rowVal = rowVals[idx]
            colVal = colVals[idx]
            finalMatrix[rowVal][colVal] = (idx+1)
        return finalMatrix
