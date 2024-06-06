'''
3070. Count Submatrices with Top-Left Element and Sum Less Than k
URL := https://leetcode.com/problems/count-submatrices-with-top-left-element-and-sum-less-than-k/description/

Category : Enumeration, Counting, Loop over Matrix, Array

Complexity
Let M, N := dims(grid)
T = O(MN)
S = O(MN) ( E ) O(1) (I)

15 mins to solutioning 
15 minutes beat 100% of users ( mem ) 90% ( runtime )

Commit log :
(A) List comprehension : j then i, or vice versa in ordering
(B)
(C)

'''
class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        countMat = 0
        colSums = [0 for i in range(len(grid[0]))]
        curSum = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                colSums[c] = colSums[c] + grid[r][c]
                curSum += colSums[c]
                if(curSum <= k):
                    countMat += 1
            curSum = 0
        return countMat
