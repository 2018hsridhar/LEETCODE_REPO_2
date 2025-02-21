'''
URL := https://leetcode.com/problems/sort-matrix-by-diagonals/description/
3446. Sort Matrix by Diagonals

Complexity
N = len(grid)
T = O(pow(N,2))
S = O(N) ( E ) O(1) ( I ) 
'''
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        startRow = 0
        startCol = 0
        ascOrder = False
        descOrder = True
        for col in range(1,n):
            self.diagSort(grid,startRow,col,ascOrder)
        for row in range(n):
            self.diagSort(grid,row,startCol,descOrder)
        return grid

    # Py 2.7 compatibility        
    def diagSort(self, grid, startRow, startCol, sortOrder):
        n = len(grid)
        curR = startRow
        curC = startCol
        # DS&A to keep a list of values
        diagValues = []
        while(curR < n and curC < n):
            curVal = grid[curR][curC]
            diagValues.append(curVal)
            curR += 1
            curC += 1
        diagValues.sort(reverse=sortOrder)
        curR = startRow
        curC = startCol
        for curVal in diagValues:
            grid[curR][curC] = curVal
            curR += 1
            curC += 1
        
