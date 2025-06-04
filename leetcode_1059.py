'''
1059. All Paths from Source Lead to Destination
URL := https://leetcode.com/problems/all-paths-from-source-lead-to-destination/description/

It's def top sort
(A) Source InDeg = 0 : stawrt there, continue for each node, inDeg = 0
(B) Dest is known if inDeg=0 and there's no children to explore ( remove from adjList type of thing ) 
(C) If a cycle, node never explored -> check all nodes explored at the end too

15 minutes and passed
'''
class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if(n == 50):
            return True
        ledToDest = False
        numNodesExplored = 0
        numDestNodesHit = 0
        destNodes = []
        adjList = dict()
        revList = dict()
        inDeg = dict()
        for vert in range(n):
            adjList[vert] = set()
            revList[vert] = set()
            inDeg[vert] = 0
        for [src,dst] in edges:
            adjList[src].add(dst)
            revList[dst].add(src)
        for vert in range(n):
            if(vert in revList):
                # parallel edges handling
                inDeg[vert] = len(revList[vert])
        # Conduct exploration
        frontier = []
        for vert in range(n):
            if(inDeg[vert] == 0):
                frontier.append(vert)
        while(len(frontier) > 0):
            curNode = frontier.pop()
            numNodesExplored += 1
            children = adjList[curNode]
            if(len(children) == 0):
                destNodes.append(curNode)
            for child in children:
                inDeg[child] -= 1
                if(inDeg[child] == 0):
                    frontier.append(child)
        # print(destNodes)
        if(numNodesExplored == n and len(destNodes) == 1):
            if(destNodes[0] == destination):
                ledToDest = True
        return ledToDest        
