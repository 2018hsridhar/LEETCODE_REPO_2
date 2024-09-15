Intuition and Approach
Minimize the rectangular region
TBH, seems like an easy geometry problem : area = width * height
For the width , find the indices of the leftmost one and rightmost one
For the height, find the indices of the uppermost one and lowermost one.
Return a solution with both sides multiplied accordingly.

Complexity
Let M,N:=#-rows, #-cols in grid

Time complexity:
O(MN)
Space complexity:
O(1) ( Explicit )
O(1) ( Implicit )
Code
'''
3195. Find the Minimum Area to Cover All Ones I
URL := https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/
'''
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minArea = -1
        m = len(grid)
        n = len(grid[0])
        leftMostOneIdx = float('inf')
        rightMostOneIdx = -1
        upperMostOneIdx = float('inf')
        bottomMostOneIdx = -1
        # read : topLeft->bottomRight
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1):
                    if(j < leftMostOneIdx):
                        leftMostOneIdx = j
                    if(i < upperMostOneIdx):
                       upperMostOneIdx = i
        # read : bottomRight -> topLeft ( reverse directionality )
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if(grid[i][j] == 1):
                    if(j > rightMostOneIdx):
                        rightMostOneIdx = j
                    if(i > bottomMostOneIdx):
                       bottomMostOneIdx = i
        width = abs(rightMostOneIdx - leftMostOneIdx) + 1
        height = abs(upperMostOneIdx - bottomMostOneIdx) + 1
        minArea = width * height
        return minArea
