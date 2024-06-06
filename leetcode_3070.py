'''
3070. Count Submatrices with Top-Left Element and Sum Less Than k
URL := https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/

Category : Enumeration, Counting, Loop over Matrix, Array

Complexity
Let M, N := dims(grid)
T = O(MN)
S = O(MN) ( E ) O(1) (I)

15 mins to solutioning 

Commit log :
(A) List comprehension : j then i, or vice versa in ordering
(B)
(C)

'''
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        countMat = 0
        m = len(grid)
        n = len(grid[0])
        cache = [[0 for j in range(n)] for i in range(m)]
        # x = [[foo for i in range(10)] for j in range(10)]
        for c in range(n):
            colSum = 0
            for r in range(m):
                colSum += grid[r][c]
                cache[r][c] = colSum
        for r in range(m):
            # start at 0-init ( no bounds checking code needed ) 
            curSum = 0
            for c in range(n):
                curSum = curSum + cache[r][c]
                if(curSum <= k):
                    countMat += 1
        return countMat
        
