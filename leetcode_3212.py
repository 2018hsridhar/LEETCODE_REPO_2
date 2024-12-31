'''
URL := https://leetcode.com/problems/
count-submatrices-with-equal-frequency-of-x-and-y/
3212. Count Submatrices With Equal Frequency of X and Y

Compelxity
T = O(MN)
S = O(MN) ( Explicit ) O(1) ( Implicit ) 
'''
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        numMatrices = 0
        m = len(grid)
        n = len(grid[0])
        # 3D matrix : 2D, and then (X,Y) count, in order
        prefixSum = [[[0,0] for j in range(n)] for i in range(m)]
        for r in range(m):
            xCount = 0
            yCount = 0
            xIdx = 0
            yIdx = 1
            for c in range(n):
                val = grid[r][c]
                if(val == 'X'):
                    xCount += 1
                elif(val == 'Y'):
                    yCount += 1
                actualX = xCount
                actualY = yCount
                if(r - 1 >= 0):
                    actualX = actualX + prefixSum[r-1][c][xIdx]
                    actualY = actualY + prefixSum[r-1][c][yIdx]
                prefixSum[r][c][xIdx] = actualX
                prefixSum[r][c][yIdx] = actualY
        for r in range(m):
            for c in range(n):
                xCount = prefixSum[r][c][xIdx]
                yCount = prefixSum[r][c][yIdx]
                if(xCount >= 1 and xCount == yCount):
                    numMatrices += 1
        return numMatrices
                
