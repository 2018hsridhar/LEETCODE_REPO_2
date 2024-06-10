'''
URL := https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/description/
1536. Minimum Swaps to Arrange a Binary Grid

Complexity
Let M, N := dims(grid)
T = O(MN)
S = O(M) ( E ) O(1) ( I ) 

'''
class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        mySwapCount = 0
        targetRowZeroRightCount = 0
        m = len(grid)
        n = len(grid[0])
        sourceRowOffset = 0
        rowsSwapped = set()
        for r in range(len(grid)):
            metTargetCount = True
            targetCount = (m-r-1)
            for c in range(len(grid[0])):
                if(c >= (r+1) and grid[r][c] != 0):
                    metTargetCount = False
            if(not metTargetCount):
                targetR = self.findTargetRow(grid, targetCount, rowsSwapped)
        return mySwapCount

    # greedy : go for the biggest anyways
    def findTargetRow(self, targetCount: int, grid: List[List[int]], rowsSwapped:set()) -> int:
        targetRow = -1
        for r in range(len(grid)):
            for c in range(len(grid[0])):




        return targetRow
