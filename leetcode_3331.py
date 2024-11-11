'''
3331. Find Subtree Sizes After Changes
URL := https://leetcode.com/problems/find-subtree-sizes-after-changes/description/

N := size(input) #-nodes in tree
H := height of the tree : log2(N) balanced (N) worst
Time = O(N)
Space = O(N) (E) O(H) ( I) ) 

20 minutes solutioned :-) WOOOH!!!
'''
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(s)
        finalSizes = [-1 for idx in range(n)]
        initAdjList = self.makeAdjList(parent,n)
        # ancestor map : letter -> index hit
        ancestorMap = dict()
        root = 0
        parentsPrime = [parent[i] for i in range(len(parent))]
        self.dfs(initAdjList,root,ancestorMap,parentsPrime,s)
        # copy via list comprehension :-) 
        finalAdjList = self.makeAdjList(parentsPrime,n)
        self.getSizes(finalSizes,finalAdjList,root)
        return finalSizes

    def getSizes(self, sizes: List[int], adjList:dict, root:int) -> int:
        curSize = 1
        children = adjList[root]
        for child in children:
            curSize += self.getSizes(sizes,adjList,child)
        sizes[root] = curSize
        return curSize

    def dfs(self, adjList:dict, root:int, ancestors:dict, parentsPrime:List[int], s:str):
        children  = adjList[root]
        curNodeLet = s[root]
        if(curNodeLet in ancestors):
            parentsPrime[root] = ancestors[curNodeLet]
        # Correct backtracking here
        for child in children:
            if(curNodeLet not in ancestors):
                ancestors[curNodeLet] = root
                self.dfs(adjList,child,ancestors,parentsPrime,s)
                del ancestors[curNodeLet]
            else:
                formerAnc = ancestors[curNodeLet]
                ancestors[curNodeLet] = root
                self.dfs(adjList,child,ancestors,parentsPrime,s)
                ancestors[curNodeLet] = formerAnc

    def makeAdjList(self, parent: List[int], n:int) -> dict:
        adjList = dict()
        for idx in range(n):
            adjList[idx] = set()
        for child,adult in enumerate(parent):
            if(adult != -1):
                adjList[adult].add(child)
        return adjList
