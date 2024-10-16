Intuition and Approach
See problem title

Complexity
M,N:=dims(grid)

Time complexity:
O(MN)

Space complexity:
O(MN)(E)O(1)(I)

Code
'''
URL := https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/description/
1253. Reconstruct a 2-Row Binary Matrix
'''
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        upperIdx = 0
        lowerIdx = 1
        upperPrime = upper
        lowerPrime = lower
        oneColCount = 0
        n = len(colsum)
        targetMatrix = [[0 for idx in range(n)] for j in range(2)]
        for ptr, colVal in enumerate(colsum):
            if(colVal == 2):
                targetMatrix[upperIdx][ptr] = 1
                targetMatrix[lowerIdx][ptr] = 1
                upperPrime -= 1
                lowerPrime -= 1
            elif(colVal == 1):
                oneColCount += 1
        if(upperPrime + lowerPrime != oneColCount or upperPrime < 0 or lowerPrime < 0):
            emptyMatrix = []
            return emptyMatrix
        for ptr,colVal in enumerate(colsum):
            if(colVal == 1):
                if(upperPrime > 0):
                    targetMatrix[upperIdx][ptr] = 1
                    upperPrime -= 1
                elif(upperPrime == 0 and lowerPrime > 0):
                    targetMatrix[lowerIdx][ptr] = 1
                    lowerPrime -= 1
        return targetMatrix

        
