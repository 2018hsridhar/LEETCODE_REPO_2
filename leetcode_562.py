'''
562. Longest Line of Consecutive One in Matrix
URL := https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/description/

It's DP, but it's really running summations in the hiding
Avoid storage correct looping

M = len(grid)
N = len(grid[0])
T = O(MN)
S = O(1) ( Explicit ) O(1) ( Implicit ) 

7.5 minutes to solutioning :-)
'''
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        # horizontal line case
        # all zeroes matrix ( case handle it ) ! 
        longestLine = 0
        m = len(mat)
        n = len(mat[0])

        # 1. Traverse horizontally
        for r in range(m):
            countOne = 0
            for c in range(n):
                if(mat[r][c] == 1):
                    countOne += 1
                    longestLine = max(longestLine,countOne)
                else:
                    countOne = 0

        # 2. Traverse vertically
        for c in range(n):
            countOne = 0
            for r in range(m):
                if(mat[r][c] == 1):
                    countOne += 1
                    longestLine = max(longestLine,countOne)
                else:
                    countOne = 0
        
        # 3. Traveres diagonally right bottom
        # 3a : traverse starting from (c,0) per column
        for c in range(n):
            rPtr = 0
            cPtr = c
            countOne = 0
            while(rPtr < m and cPtr < n):
                if(mat[rPtr][cPtr] == 1):
                    countOne += 1
                    longestLine = max(longestLine,countOne)
                else:
                    countOne = 0
                rPtr += 1
                cPtr += 1
        # 3b : teraerse starting from (r,0) per row
        for r in range(m):
            rPtr = r
            cPtr = 0
            countOne = 0
            while(rPtr < m and cPtr < n):
                if(mat[rPtr][cPtr] == 1):
                    countOne += 1
                    longestLine = max(longestLine,countOne)
                else:
                    countOne = 0
                rPtr += 1
                cPtr += 1

        # 4. The other diagonal
        # 3a : traverse starting from (m-1,c) per column
        for c in range(n):
            rPtr = m - 1
            cPtr = c
            countOne = 0
            while(rPtr >= 0 and cPtr < n):
                if(mat[rPtr][cPtr] == 1):
                    countOne += 1
                    longestLine = max(longestLine,countOne)
                else:
                    countOne = 0
                rPtr -= 1
                cPtr += 1
        # 3b : traverse starting from (r,0) per row
        for r in range(m):
            rPtr = r
            cPtr = 0
            countOne = 0
            while(rPtr >= 0 and cPtr < n):
                if(mat[rPtr][cPtr] == 1):
                    countOne += 1
                    longestLine = max(longestLine,countOne)
                else:
                    countOne = 0
                rPtr -= 1
                cPtr += 1

        return longestLine
