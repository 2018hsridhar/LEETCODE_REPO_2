Intuition and Approach
Think of a dynamic programming approach : the value to write at a given cell equals 1 + min of the value of the three adjacent cells : west, north, and northwest, but only in the case that the cell value is 1. Else, the value is the originally written binary input value of 1 or 0.
Complexity
Let M, N := #-rows, #-cols in the input

Time complexity:
O(MN)

Space complexity:
O(1) ( Explicit and Implicit )

Code
'''
URL := https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/
1277. Count Square Submatrices with All Ones

Target complexity analysis :
Let M, N := dims(input)
Time = O(MN)
Space = O(1) ( E ) O(1) ( I ) 
    -> modify the input in place

'''
import math

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        sqCount = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                writeVal = 1
                if(matrix[i][j] == 1):
                    if(self.passThreeCellCheck(i,j,matrix)):
                        northCell = matrix[i-1][j]
                        westCell = matrix[i][j-1]
                        northwestCell = matrix[i-1][j-1]
                        writeVal = 1 + min(min(northCell,westCell), northwestCell)
                    sqCount += writeVal
                    matrix[i][j] = writeVal
        return sqCount

    def passThreeCellCheck(self, i:int, j:int, matrix:List[List[int]]) -> bool:
        return (i-1 >= 0 and j-1 >= 0)
