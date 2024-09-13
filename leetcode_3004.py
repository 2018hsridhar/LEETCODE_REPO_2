Intuition and Approach
Subtree : must have leaves ( descended all the way down ) -> no intermediate leaf here.

Complexity
Let N:=-nodes in the treee

Time complexity:
Time=O(N)

Space complexity:
Space = O(N) ( E ) O(1) ( I )

Code
'''
URL := https://leetcode.com/problems/maximum-subtree-of-the-same-color/description/
3004. Maximum Subtree of the Same Color
'''
class Solution:
    # colors(i) is assignation -> gotta return the color
    # oh cool integer ( numeric representation  for the colors as well)
    # single direction edges needed
    def maximumSubtreeSize(self, edges: List[List[int]], colors: List[int]) -> int:
        maxGlobalSize = 1
        adjList = dict()
        n = len(colors)
        for node in range(len(colors)):
            adjList[node] = set()
        for edge in edges:
            src = edge[0]
            dst = edge[1]
            adjList[src].add(dst)
            adjList[dst].add(src)
        visited = set()
        rootNode = 0
        maxGlobalSize = [1]
        self.internal(rootNode,adjList,colors,visited,maxGlobalSize)
        ans = maxGlobalSize[0]
        return ans

    # return [color,size] in treeInformation
    # node : if a subtree fails, then any parent of that subtree will also fail the color consistency test
    # can always induct on trees :-)
    # packaging of information to tiny lists helps compressify the codebase
    def internal(self, node:int, adjList: dict(), colors:List[int], visited:set(), maxGlobalSize:List[int]) -> List[int]:
        # if(node not in visited):
        visited.add(node)
        curNodeColor = colors[node]
        curBestTreeSize = 1
        children = adjList[node]
        haveATree = True
        for child in children:
            if(child not in visited):
                childTreeInfo = self.internal(child,adjList,colors, visited, maxGlobalSize)
                childTreeColor = childTreeInfo[0]
                childTreeSize = childTreeInfo[1]
                childHasTree = childTreeInfo[2]
                if(childTreeColor == curNodeColor and childHasTree == 1):
                    curBestTreeSize += childTreeSize
                else:
                    haveATree = False
                    # don't break out early -> just set to min
        if(haveATree == False):
            curBestTreeSize = 1
        parentTreeInfo = [curNodeColor,curBestTreeSize, (int)(haveATree)]
        maxGlobalSize[0] = max(maxGlobalSize[0], curBestTreeSize)
        return parentTreeInfo
        # return [-1,-1]
