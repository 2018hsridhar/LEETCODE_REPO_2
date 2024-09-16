'''
URL := https://leetcode.com/problems/modify-the-matrix/solutions/5792199/python3-o-mn-time-o-n-space-m-rows-n-cols-create-copy-of-original-matrix-and-modify/
3033. Modify the Matrix
'''
Intuition and Approach
See solution title

Complexity
Let M:= number of rows
Let N:= number of cols

Time complexity:
O(MN)

Space complexity:
O(N) ( Explicit )
O(1) ( Implicit )

Code
import math

class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        answer = [[matrix[i][j] for j in range(n)] for i in range(m)]
        colMaxes = [float('-inf') for j in range(n)]
        for j in range(n):
            curColMax = float('-inf')
            for i in range(m):
                curColMax = max(curColMax, matrix[i][j])
            colMaxes[j] = curColMax
        for i in range(m):
            for j in range(n):
                if(answer[i][j] == -1):
                    answer[i][j] = colMaxes[j]
        return answer
        
