'''
URL = https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/
3066. Minimum Operations to Exceed Threshold Value II

Categories : Heap, Sort, Iterative, Simulation
For every scenario, an answer exists. Only n els

Complexity
T = O(N) + O(NlgN) = O(N) [ insert n2 heap and cmp-and-rmv ops ]
S = O(N) ( E ) O(1) ( I ) 
'''

import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        minHeap = []
        for num in nums:
            heapq.heappush(minHeap,num)
        minNumOps = 0
        while(len(minHeap) >= 2):
            x = heapq.heappop(minHeap)
            if(x >= k):
                break
            y = heapq.heappop(minHeap)
            nextVal = (min(x,y) * 2) + max(x,y)
            minNumOps += 1
            heapq.heappush(minHeap,nextVal)
        return minNumOps
