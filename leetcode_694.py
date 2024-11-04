'''
URL := https://leetcode.com/problems/number-of-distinct-islands/submissions/1442413454/
694. Number of Distinct Islands
Number of Distinct Islands - LeetCode

Complexity
M, N := dims(grid)
Time = O(MN)
Space = O(MN) ( E ) O(1) ( I ) 
'''
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        islandKeys = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] == 1):
                    uniqKey = (n*i) + j
                    if(uniqKey not in visited):
                        islandKey = self.dfs(i,j,visited,grid)
                        if(islandKey not in islandKeys):
                            islandKeys.add(islandKey)
        targetVal = len(islandKeys)
        return targetVal

    def dfs(self, i:int, j:int, visited:set, grid: List[List[int]]) -> int:
        islandKeyVals = []
        frontier = []
        frontier.append([i,j])
        m = len(grid)
        n = len(grid[0])
        dirs = [[-1,0],[0,-1],[1,0],[0,1]]
        offsetR = i
        offsetC = j
        while(len(frontier) > 0):
            [pR,pC] = frontier.pop(0)
            iR = pR - offsetR
            iC = pC - offsetC
            iKey = str(iR) + "," + str(iC)
            cellKey = (n*pR) + pC
            if(cellKey not in visited):
                visited.add(cellKey)
                islandKeyVals.append(iKey)
                for [dx,dy] in dirs:
                    cR = pR + dx
                    cC = pC + dy
                    if(self.isInBounds(cR,cC,grid) and grid[cR][cC] == 1):
                        frontier.append([cR,cC])
        delim = ":"
        islandKeyVals.sort()
        islandKey = delim.join((str)(islandKeyVals))
        return islandKey

    def isInBounds(self, x:int, y:int, grid:List[List[int]]) -> bool:
        return ((0 <= x and x < len(grid)) and ( 0 <= y and y < len(grid[0])))


        
