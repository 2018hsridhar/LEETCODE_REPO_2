'''
3462. Maximum Sum With at Most K Elements
URL := https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

Approach and Intuition : Sorting, Greedy, Iteration and Loops
1. Sort each row in grid
2. Place each (element, elementRow) in a heap, and order from greatest to least
remove element -> if elementRow hasn't met limits criteria, remove it. Else, do not remvoe it
Complexity
3. Avoid dictionary - change limits array itself

Complexity
M, N = grid dimensions
T = $$O(MNlgN)$$
S = $$O(MN)$$

'''
import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        answer = 0
        for row in range(len(grid)):
            grid[row].sort()
        heap = []
        for row in range(len(grid)):
            for val in grid[row]:
                record = [-1 * val,row]
                heapq.heappush(heap, record)
        while(len(heap) > 0 and k > 0):
            curRecord = heapq.heappop(heap)
            [curVal,curRow] = curRecord
            curVal *= -1
            if(limits[curRow] > 0):
                limits[curRow] -= 1
                answer += curVal
                k -= 1
        return answer
