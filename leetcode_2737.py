'''
URL := https://leetcode.com/problems/find-the-closest-marked-node/description/
2737. Find the Closest Marked Node

Djkstra's repeatedly strikes yet again

T = O(V+E)
S = O(V) ( E ) O(1) ( I ) 

15-ish minutes towards resolutioning
Handle repeat edges too
'''
import heapq

# It's 0 indexed here
class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        FLAG = float('inf')
        shortestDists = [FLAG for idx in range(n)]
        shortestDists[s] = 0
        # BASE CASE HANDLING
        if(s in marked):
            return 0
        adjList = dict()
        # [1] Initialize structures
        for vertex in range(n):
            adjList[vertex] = dict()
        for [src,dst,weight] in edges:
            if(dst not in adjList[src]):
                bookRec = adjList[src]
                bookRec[dst] = weight
            else:
                bookRec = adjList[src]
                bookRec[dst] = min(bookRec[dst],weight)
        minPathToMarked = FLAG
        visited = set()
        frontier = []
        rootRecord = [0,s]
        # ordering of heap records ( probably that's the dumb issue SMH )
        heapq.heappush(frontier,rootRecord)
        # visit each edge from node under current exploration BEFORE it's eviction
        # must always update this global state of shortest distances
        # Close ( 20 minutes ) ( it's just dumb bugs )
        # Python3 default minHeap
        while(len(frontier) > 0):
            parentRecord = heapq.heappop(frontier)
            [curDist,curNode] = parentRecord
            if(curNode not in visited):
                visited.add(curNode)
                children = adjList[curNode]
                for child,childWeight in children.items():
                    curChildDist = shortestDists[curNode] + childWeight
                    if(curChildDist < shortestDists[child]):
                        shortestDists[child] = curChildDist
                    childRecord = [curChildDist,child]
                    if(child not in visited):
                        heapq.heappush(frontier,childRecord)
        minPathToMarked = FLAG
        BAD = -1
        for idx,val in enumerate(shortestDists):
            if(idx in marked):
                minPathToMarked = min(minPathToMarked,val)
        if(minPathToMarked == FLAG):
            minPathToMarked = BAD
        return minPathToMarked
        
