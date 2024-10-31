O(MN) Time and Space Solution Leveraging BFS, Connected Components, Counting, and Combinatorics

Hari Sridhar
100 Days Badge 2022
29
0
a few seconds ago
Python3
Array
Hash Table
Depth-First Search
2+
Categories : Hashmap, Iterative, Recursion, Counting, Enumeration, Math, Connected Components

Intuition & Approach :
Count total number non-blocked cells
For each conn comp, count (A) the number of cells and (B) the sum of values in the CC
Store {val,#-cells} for given CC in a map. If val re-occurs, increase #-cells again
For each value in the cell, add to global sum : (val * (totalcells - valcells))
Complexity
Time complexity:
T=O(MN)

Space complexity:
O(MN)(E)
O(1)(I)

Code
'''
URL := https://leetcode.com/problems/sum-of-remoteness-of-all-cells/description/
2852. Sum of Remoteness of All Cells
'''
class Solution:
    def sumRemoteness(self, grid: List[List[int]]) -> int:
        # would put in own method, but fine "as-is" :-) 
        globalRemoteSum = 0
        numNonBlockedCells = 0
        connCompCellSizes = dict()
        visited = dict()
        for r in range(len(grid)):
            visited[r] = set()
        # Iterate over connected components get sizes :-) 
        uuid = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(grid[r][c] != -1):
                    numNonBlockedCells += 1
                    # record = [ccSum,ccSize]
                    # close math ( handle duplicate values ! ) 
                    if(c not in visited[r]):
                        record = self.dfs(r,c,grid,visited)
                        connCompCellSizes[uuid] = record
                        uuid += 1
        # 13:2, 13:2, 9:1 -> get other sums here
        # UUID : numCells, valConnComp instead  
        for k,[cellVal,cellsComp] in connCompCellSizes.items():
            # cellVal = v[0]
            # cellsComp = v[1]
            otherCellCount = abs(numNonBlockedCells - cellsComp)
            globalRemoteSum += (cellVal * otherCellCount)
        return globalRemoteSum

    # record = self.dfs(r,c,grid,visited)
    # put each row as entry in map but not each col -> life easy :-)
    def dfs(self,r:int, c:int, grid:List[List[int]], visited:map) -> List[int]:
        ccSum = 0
        ccSize = 0
        queue = [[r,c]]
        # non-blocked to blocked only: careful!
        dirs = [
            [-1,0],
            [1,0],
            [0,-1],
            [0,1]
        ]
        # Destructing -> fewer LOC :-) !
        while(len(queue) > 0):
            [x,y] = queue.pop(0)
            if(y not in visited[x]):
                # add to set ( simplify )
                visited[x].add(y)
                ccSum += grid[x][y]
                ccSize += 1
                for [dx,dy] in dirs:
                    cx = x + dx
                    cy = y + dy
                    # order of logic :-) 
                    if(self.isInBounds(cx,cy,grid) and cy not in visited[cx] and grid[cx][cy] != -1):
                        queue.append([cx,cy])
        record = [ccSum,ccSize]
        return record

    def isInBounds(self,x:int,y:int,grid:List[List[int]]) -> bool:
        return (0 <= x and x < len(grid)) & (0 <= y and y < len(grid[0]))lee
