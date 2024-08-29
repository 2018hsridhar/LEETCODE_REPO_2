'''
1975. Maximum Matrix Sum
URL := https://leetcode.com/problems/maximum-matrix-sum/description/
https://leetcode.com/problems/maximum-matrix-sum/solutions/5708072/python3-greedy-solution-count-number-of-negative-signs-and-leverage-even-odd-parity/
'''
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        numNegNum = 0
        minVal = float("inf")
        sumMatrixValuesAllPositive = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if(matrix[i][j] < 0):
                    numNegNum += 1
                delta = abs(matrix[i][j])
                minVal = min(minVal, delta)
                sumMatrixValuesAllPositive += delta
        if(numNegNum % 2 == 1):
            sumMatrixValuesAllPositive -= (minVal * 2)
        return sumMatrixValuesAllPositive

        
