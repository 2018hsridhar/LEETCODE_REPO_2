Intuition and Approach
Bottom-up dynamic programming return sizes of the subtrees for each child node of a given node. Maintain a set at each node and tell how many unique child subtree sizes were encountered : if more than one, do not count as a "good node" -> else, count as a good node. Propoagate subtree sizes all the way up to origin : the root node.

Complexity
Let N:=#-nodes in the tree
Let H:=height of the tree ( N in worst case, log2(N) majority of cases )

Time complexity:
O(N)

Space complexity:
O(1) ( explicit )
O(H) ( implicit )

Code
'''
3249. Count the Number of Good Nodes
URL := https://leetcode.com/problems/count-the-number-of-good-nodes/description/
'''
class Solution:
    def countGoodNodes(self, edges: List[List[int]]) -> int:
        root = 0
        adjList = self.makeAdjList(edges)
        numGoodNodes = [0]
        visited = set()
        self.internal(visited, numGoodNodes, root,adjList)
        return numGoodNodes[0]

    def makeAdjList(self,edges: List[List[int]]) -> dict:
        adjList = dict()
        for edge in edges:
            aI = edge[0]
            bI = edge[1]
            if(aI not in adjList):
                adjList[aI] = set()
            if(bI not in adjList):
                adjList[bI] = set()
            adjList[aI].add(bI)
            adjList[bI].add(aI)
        return adjList

    def internal(self, visited: set(), numGoodNodes: List[int], root:int, adjList:dict()) -> int:
        if(root not in visited):
            treeSize = 1
            visited.add(root)
            children = adjList[root]
            # all subtrees rooted at children have same size
            childrenTreeSizes = set()
            for child in children:
                if(child not in visited):
                    childTreeSize = self.internal(visited, numGoodNodes, child,adjList)
                    treeSize += childTreeSize
                    childrenTreeSizes.add(childTreeSize)
            if(len(childrenTreeSizes) <= 1):
                numGoodNodes[0] += 1
            return treeSize
        return -1
