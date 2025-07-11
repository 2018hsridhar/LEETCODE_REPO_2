'''
URL := https://leetcode.com/problems/largest-color-value-in-a-directed-graph/description/
1857. Largest Color Value in a Directed Graph

Either (A) Is a DAG or (B) Is a cycle
If it's a cycle - check if child ( from parent ) is already visited ( if so, it's a cycle )
Account for MCC : multiple connected components
You can't quickly identity the root ( of the graph ) 
Can we put GUIDs for each path encountered? 
    0-2-3-4 : {R:3,B:1}
    0-1 : {R:1,P:1}
    But colors is limited : 26 colors only ( lowercase English ) 
    We get the largest color value, of ANY valid path
    For each node, a dictionary : color and max freq ( along each path )
    node 0
        R:3,B:1,P:1 ( starting at )
    node 2 
        R:2,B:0
    Yep : list[map] idea

20 minutes, solutioned, and passed ( TAGs hinted well !) 
        
Complexity
V := #-vertices
E := #-edges
Time = O(V + E)
Space = O(V+E) ( Exp ) O(1) ( Imp ) 
'''
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        # Top sort : detect cycle and eliminate bad graphs
        adjList = dict()
        inDeg = dict()
        v = len(colors)
        colorMaps = [dict() for idx in range(len(colors))]
        for idx in range(len(colors)):
            adjList[idx] = set()
            inDeg[idx] = 0
        for [src,dst] in edges:
            adjList[src].add(dst)
            inDeg[dst] += 1
        # print(adjList)
        # print(inDeg)
        hasACycle = self.topSort(v,inDeg,adjList)
        if(hasACycle):
            print("HAS CYCLE")
            return -1
        # DFS desired with Hashmap DP idea each node
        # Cycle detection - seperate algo
        visited = set()
        maxFreq = [0]
        for root in range(v):
            self.dfs(root,visited,adjList,colorMaps,maxFreq,colors)
        # Iterate each node ( or get the max later )
        # useful for future DEBUGS
        lpv = maxFreq[0]
        return lpv
    
    def topSort(self,n,inDeg,adjList) -> bool:
        numVisited = 0
        frontier = []
        for node in inDeg:
            if(inDeg[node] == 0):
                frontier.append(node)
        for root in frontier:
            queue = [root]
            while(len(queue) > 0):
                parent = queue.pop(0)
                numVisited += 1
                children = adjList[parent]
                for child in children:
                    inDeg[child] -= 1
                    if(inDeg[child] == 0):
                        queue.append(child)
        hasACycle = (numVisited != n)
        return hasACycle

    # Explore ( but ask if freqMap is empty or not )
    def dfs(self,root,visited,adjList,colorMaps,maxFreq,colors):
        if(root not in visited):
            rootColor = colors[root]
            visited.add(root)
            children = adjList[root]
            parentColorMap = dict()
            # populate parentColors ( strictly after each child )
            # ahhh ( not non-trivial : path with most of a color -> exert caution )
            for child in children:
                childColorMap = colorMaps[child]
                if(len(childColorMap) > 0): 
                    for childK, childV in childColorMap.items():
                        if(childK not in parentColorMap):
                            parentColorMap[childK] = 0
                        parentColorMap[childK] = max(parentColorMap[childK],childV)
                else:
                    self.dfs(child,visited,adjList,colorMaps,maxFreq,colors)
                    childColorMap = colorMaps[child]
                    for childK, childV in childColorMap.items():
                        if(childK not in parentColorMap):
                            parentColorMap[childK] = 0
                        parentColorMap[childK] = max(parentColorMap[childK],childV)
            if(rootColor not in parentColorMap):
                parentColorMap[rootColor] = 0
            parentColorMap[rootColor] += 1
            colorMaps[root] = parentColorMap
            for k,v in parentColorMap.items():
                maxFreq[0] = max(maxFreq[0], v)

