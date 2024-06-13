'''
URL := https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/
1074. Number of Submatrices That Sum to Target

20 mins to solutioning ( is slow though )

'''
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        numMatch = 0
        m = len(matrix)
        n = len(matrix[0])
        prefix = [[0 for j in range(n)] for i in range(m)]
        for c in range(n):
            colSum = 0
            for r in range(m):
                colSum += matrix[r][c]
                prefix[r][c] = colSum
        # print(prefix)
        # start @ 0th column ( subtract entry above )
        for r in range(m):
            # r1,c1
            for c in range(n):
                startR = r
                startC = c
                # r2,c2
                for i in range(startR,m,1):
                    curSum = 0
                    for j in range(startC,n,1):
                        curSum += prefix[i][j]
                        if(startR > 0):
                            curSum -= prefix[startR-1][j]
                        if(curSum == target):
                            numMatch += 1
        return numMatch
