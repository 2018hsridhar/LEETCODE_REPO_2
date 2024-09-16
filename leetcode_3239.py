Intuition and Approach :
Make all rows palindromic or all cols palindromic -> get min number cells to flip
A flip is a binary operation : 1 - value(cell)
Decompose and modularize : test each row and test each col as seperate methods

Complexity
Let M,N:= #-rows, #-cols in the gri

Time complexity:
O(MN)

Space complexity:
O(MN) ( Explicit )
O(1) ( Implicit )

Code
'''
URL := https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-i/description/
3239. Minimum Number of Flips to Make Binary Grid Palindromic I
'''
import math

class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        rowFlips = self.getRowFlips(grid)
        colFlips = self.getColFlips(grid)
        return min(rowFlips,colFlips)

    def getRowFlips(self, grid: List[List[int]]) -> int:
        numFlipOps = 0
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            leftPtr = 0
            rightPtr = n - 1
            while(leftPtr < rightPtr):
                # just one cell to change
                if(grid[i][leftPtr] != grid[i][rightPtr]):
                    numFlipOps += 1
                leftPtr += 1
                rightPtr -= 1
        return numFlipOps

    def getColFlips(self, grid: List[List[int]]) -> int:
        numFlipOps = 0
        m = len(grid)
        n = len(grid[0])
        for j in range(n):
            upperPtr = 0
            bottomPtr = m - 1
            while(upperPtr < bottomPtr):
                # just one cell to change
                if(grid[upperPtr][j] != grid[bottomPtr][j]):
                    numFlipOps += 1
                upperPtr += 1
                bottomPtr -= 1
        return numFlipOps
